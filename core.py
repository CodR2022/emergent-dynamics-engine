from dataclasses import dataclass


@dataclass
class Params:
    """
    Parameters controlling the emergent system.
    """

    alpha: float = 0.60
    beta: float = 0.40
    gamma: float = 0.30
    delta: float = 0.20
    delay: int = 3

    noise: float = 0.01
    instability_threshold: float = 0.25

    strength_learning_rate: float = 0.05
    strength_min: float = 0.10
    strength_max: float = 3.00

    local_radius: int = 1
    long_radius: int = 3

    seed: int | None = None
