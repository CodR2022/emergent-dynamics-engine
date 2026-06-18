from **future** import annotations

import numpy as np

def laplacian(grid: np.ndarray) -> np.ndarray:
"""
Discrete 2D Laplacian using nearest neighbors.

```
This measures local difference and supports diffusion/coherence.
"""
return (
    np.roll(grid, 1, axis=0)
    + np.roll(grid, -1, axis=0)
    + np.roll(grid, 1, axis=1)
    + np.roll(grid, -1, axis=1)
    - 4 * grid
)
```

def bi_laplacian(grid: np.ndarray) -> np.ndarray:
"""
Bi-Laplacian operator.

```
Used as a higher-order spacing / anti-collapse term.
"""
return laplacian(laplacian(grid))
```

def weighted_neighborhood_average(
grid: np.ndarray,
strength: np.ndarray,
radius: int,
) -> np.ndarray:
"""
Weighted neighborhood average over a square radius.

```
Stronger/stabler regions influence the field more.
"""
if radius <= 0:
    return grid

total = np.zeros_like(grid, dtype=float)
weight_total = np.zeros_like(grid, dtype=float)

for dx in range(-radius, radius + 1):
    for dy in range(-radius, radius + 1):
        shifted_grid = np.roll(np.roll(grid, dx, axis=0), dy, axis=1)
        shifted_strength = np.roll(np.roll(strength, dx, axis=0), dy, axis=1)

        total += shifted_grid * shifted_strength
        weight_total += shifted_strength

return total / np.maximum(weight_total, 1e-9)
```

def normalize_grid(grid: np.ndarray) -> np.ndarray:
"""
Normalize grid values to 0..1 for plotting.
"""
minimum = np.min(grid)
maximum = np.max(grid)

```
if maximum - minimum < 1e-12:
    return np.zeros_like(grid)

return (grid - minimum) / (maximum - minimum)
```
