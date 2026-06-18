from .core import laplacian, bi_laplacian, weighted_neighborhood_average


def diffusion_term(state, delayed, strength, params):
    """
    Local attraction / smoothing.

    Pulls neighboring values toward local coherence.
    """
    return params.alpha * laplacian(delayed)


def repulsion_term(state, delayed, strength, params):
    """
    Anti-collapse / spacing term.

    Prevents everything from collapsing into one center.
    """
    return -params.beta * bi_laplacian(delayed)


def nonlinear_amplification_term(state, delayed, strength, params):
    """
    Nonlinear amplification.

    Strong local values reinforce themselves and can create attractor-like centers.
    """
    return params.gamma * (state ** 2)


def delay_term(state, delayed, strength, params):
    """
    Finite propagation / delayed communication.

    Nodes respond to older information, not the instantaneous present.
    This prevents perfect synchronization and keeps dynamics alive.
    """
    return -params.delta * (state - delayed)


def local_attraction_long_repulsion_term(state, delayed, strength, params):
    """
    Layered neighborhood interaction.

    Local attraction plus longer-range repulsion creates stable spacing,
    repeated structures, and particle-like clusters.
    """
    local = weighted_neighborhood_average(delayed, strength, params.local_radius)
    distant = weighted_neighborhood_average(delayed, strength, params.long_radius)
    return (local - state) * params.alpha - (distant - local) * params.beta


def damping_term(state, delayed, strength, params):
    """
    Soft damping.

    Useful for preventing runaway growth in parameter experiments.
    """
    return -0.01 * state


DEFAULT_TERMS = [
    diffusion_term,
    repulsion_term,
    nonlinear_amplification_term,
    delay_term,
]

LAYERED_TERMS = [
    local_attraction_long_repulsion_term,
    nonlinear_amplification_term,
    delay_term,
]
