from __future__ import annotations

from emergent import Params, Simulation
from emergent.execution import EquationEngine
from emergent import terms
from emergent.utils import plot_snapshots


def run_mode(name: str, engine: EquationEngine, params: Params):
    sim = Simulation(
        size=80,
        params=params,
        engine=engine,
    )

    snapshots = sim.run(
        steps=250,
        capture_steps=[50, 100, 150, 250],
    )

    plot_snapshots(
        snapshots,
        title=f"Mode: {name}",
        save_path=f"outputs/{name.lower().replace(' ', '_')}.png",
    )

    print(f"{name} final metrics:", sim.metrics[-1])


def main():
    params = Params(
        alpha=0.60,
        beta=0.40,
        gamma=0.25,
        delta=0.20,
        delay=3,
        noise=0.01,
        instability_threshold=0.25,
        seed=42,
    )

    modes = {
        "Attraction Only": EquationEngine([
            terms.diffusion_term,
        ]),
        "Repulsion Only": EquationEngine([
            terms.repulsion_term,
        ]),
        "Attraction Repulsion": EquationEngine([
            terms.diffusion_term,
            terms.repulsion_term,
        ]),
        "Layered Full": EquationEngine([
            terms.local_attraction_long_repulsion_term,
            terms.nonlinear_amplification_term,
            terms.delay_term,
        ]),
    }

    for name, engine in modes.items():
        run_mode(name, engine, params)


if __name__ == "__main__":
    main()
