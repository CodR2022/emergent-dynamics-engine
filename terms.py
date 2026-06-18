import numpy as np


def laplacian(grid: np.ndarray) -> np.ndarray:
    """
    Discrete 2D Laplacian using wrapped boundaries.

    Interpreted here as attraction / smoothing / local diffusion.
    """
    return (
        np.roll(grid, 1, axis=0)
        + np.roll(grid, -1, axis=0)
        + np.roll(grid, 1, axis=1)
        + np.roll(grid, -1, axis=1)
        - 4 * grid
    )


def bi_laplacian(grid: np.ndarray) -> np.ndarray:
    """
    Laplacian of the Laplacian.

    Used here as a spacing / anti-collapse / repulsion term.
    """
    return laplacian(laplacian(grid))


def weighted_neighborhood_average(
    grid: np.ndarray,
    strength: np.ndarray,
    radius: int,
) -> np.ndarray:
    """
    Weighted average over a square neighborhood using wrapped boundaries.

    Stronger/stabilized regions influence future behavior more.
    """
    total = np.zeros_like(grid, dtype=float)
    total_weight = np.zeros_like(grid, dtype=float)

    for di in range(-radius, radius + 1):
        for dj in range(-radius, radius + 1):
            shifted_grid = np.roll(np.roll(grid, di, axis=0), dj, axis=1)
            shifted_weight = np.roll(np.roll(strength, di, axis=0), dj, axis=1)
            total += shifted_grid * shifted_weight
            total_weight += shifted_weight

    return total / np.maximum(total_weight, 1e-12)


def normalize_grid(grid: np.ndarray) -> np.ndarray:
    low = np.min(grid)
    high = np.max(grid)
    if high - low < 1e-12:
        return np.zeros_like(grid)
    return (grid - low) / (high - low)
