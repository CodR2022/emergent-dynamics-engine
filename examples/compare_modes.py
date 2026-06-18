from __future__ import annotations

from emergent import Params, Simulation
from emergent.execution import EquationEngine
from emergent import terms
from emergent.utils import plot_snapshots

def run_mode(
name: str,
engine: EquationEngine,
params: Params,
steps: int = 500,
capture_steps=None,
):
"""
Run one comparison mode and save its snapshot output.
"""
capture_steps = capture_steps or [100, 200, 350, 500]

```
sim = Simulation(
    size=80,
    params=params,
    engine=engine,
)

snapshots = sim.run(
    steps=steps,
    capture_steps=capture_steps,
)

filename = name.lower().replace(" ", "_").replace("+", "plus")

plot_snapshots(
    snapshots,
    title=f"Mode: {name}",
    save_path=f"outputs/{filename}.png",
)

print(f"{name} engine terms:", sim.engine.describe())
print(f"{name} final metrics:", sim.metrics[-1])
print(f"Saved outputs/{filename}.png")
```

def main():
"""
Compare several different rule combinations.

```
Each mode gets its own parameters so the differences are visible.
"""

modes = {
    "Attraction Only": {
        "engine": EquationEngine([
            terms.diffusion_term,
        ]),
        "params": Params(
            alpha=0.95,
            beta=0.00,
            gamma=0.00,
            delta=0.00,
            delay=1,
            noise=0.001,
            instability_threshold=0.60,
            seed=42,
        ),
    },
    "Repulsion Only": {
        "engine": EquationEngine([
            terms.repulsion_term,
        ]),
        "params": Params(
            alpha=0.00,
            beta=0.85,
            gamma=0.00,
            delta=0.00,
            delay=1,
            noise=0.001,
            instability_threshold=0.60,
            seed=42,
        ),
    },
    "Attraction + Repulsion": {
        "engine": EquationEngine([
            terms.diffusion_term,
            terms.repulsion_term,
        ]),
        "params": Params(
            alpha=0.80,
            beta=0.70,
            gamma=0.00,
            delta=0.00,
            delay=1,
            noise=0.001,
            instability_threshold=0.60,
            seed=42,
        ),
    },
    "Amplification Only": {
        "engine": EquationEngine([
            terms.nonlinear_amplification_term,
        ]),
        "params": Params(
            alpha=0.00,
            beta=0.00,
            gamma=0.35,
            delta=0.00,
            delay=1,
            noise=0.001,
            instability_threshold=0.45,
            seed=42,
        ),
    },
    "Delay Only": {
        "engine": EquationEngine([
            terms.delay_term,
        ]),
        "params": Params(
            alpha=0.00,
            beta=0.00,
            gamma=0.00,
            delta=0.45,
            delay=6,
            noise=0.002,
            instability_threshold=0.60,
            seed=42,
        ),
    },
    "Layered Full": {
        "engine": EquationEngine([
            terms.local_attraction_long_repulsion_term,
            terms.nonlinear_amplification_term,
            terms.delay_term,
        ]),
        "params": Params(
            alpha=0.90,
            beta=0.75,
            gamma=0.35,
            delta=0.30,
            delay=4,
            noise=0.002,
            instability_threshold=0.45,
            local_radius=1,
            long_radius=5,
            seed=42,
        ),
    },
}

for name, config in modes.items():
    run_mode(
        name=name,
        engine=config["engine"],
        params=config["params"],
        steps=500,
        capture_steps=[100, 200, 350, 500],
    )
```

if **name** == "**main**":
main()
