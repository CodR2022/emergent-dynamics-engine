from __future__ import annotations

import numpy as np

from .params import Params
from .execution import EquationEngine
from .terms import DEFAULT_TERMS, LAYERED_TERMS
from .core import normalize_grid


class Simulation:
    """
    Main emergent system simulation.
    """

    def __init__(
        self,
        size: int = 80,
        params: Params | None = None,
        engine: EquationEngine | None = None,
        mode: str = "layered",
    ):
        self.size = size
        self.params = params or Params()
        self.rng = np.random.default_rng(self.params.seed)

        self.state = self.rng.random((size, size))
        self.strength = np.ones((size, size), dtype=float) * 0.5
        self.history: list[np.ndarray] = []

        if engine is not None:
            self.engine = engine
        elif mode == "layered":
            self.engine = EquationEngine(LAYERED_TERMS)
        elif mode == "default":
            self.engine = EquationEngine(DEFAULT_TERMS)
        else:
            raise ValueError(f"Unknown mode: {mode}")

        self.step_count = 0
        self.metrics = []

    def delayed_state(self):
        if len(self.history) > self.params.delay:
            return self.history[-self.params.delay]
        return self.state

    def apply_entropy_noise(self, grid):
        if self.params.noise <= 0:
            return grid
        return grid + self.rng.normal(0, self.params.noise, size=grid.shape)

    def apply_instability_collapse(self, new_state):
        diff = np.abs(new_state - self.state)
        mask = diff > self.params.instability_threshold

        if np.any(mask):
            new_state = new_state.copy()
            new_state[mask] = self.rng.random(np.sum(mask))

        return new_state, diff, int(np.sum(mask))

    def update_strength(self, diff):
        self.strength += self.params.strength_learning_rate - diff
        self.strength = np.clip(
            self.strength,
            self.params.strength_min,
            self.params.strength_max,
        )

    def collect_metrics(self, collapse_count):
        metric = {
            "step": self.step_count,
            "mean": float(np.mean(self.state)),
            "std": float(np.std(self.state)),
            "min": float(np.min(self.state)),
            "max": float(np.max(self.state)),
            "strength_mean": float(np.mean(self.strength)),
            "strength_max": float(np.max(self.strength)),
            "collapse_count": collapse_count,
        }

        self.metrics.append(metric)
        return metric

    def step(self):
        self.history.append(self.state.copy())

        delayed = self.delayed_state()

        new_state = self.engine.evaluate(
            self.state,
            delayed,
            self.strength,
            self.params,
        )

        new_state = self.apply_entropy_noise(new_state)
        new_state, diff, collapse_count = self.apply_instability_collapse(new_state)

        self.update_strength(diff)

        self.state = new_state
        self.step_count += 1

        return self.collect_metrics(collapse_count)

    def run(self, steps: int = 300, capture_steps=None):
        capture_steps = set(capture_steps or [])
        snapshots = []

        for _ in range(steps):
            metric = self.step()

            if metric["step"] in capture_steps:
                snapshots.append(self.normalized_state().copy())

        return snapshots

    def normalized_state(self):
        return normalize_grid(self.state)
