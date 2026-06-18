from **future** import annotations

from dataclasses import dataclass

@dataclass
class Params:
"""
Parameter set for the emergent dynamics simulation.
"""

```
alpha: float = 0.60
beta: float = 0.40
gamma: float = 0.30
delta: float = 0.20

delay: int = 3
noise: float = 0.01
instability_threshold: float = 0.25

strength_learning_rate: float = 0.01
strength_min: float = 0.0
strength_max: float = 1.0

local_radius: int = 1
long_radius: int = 4

seed: int | None = 42
```
