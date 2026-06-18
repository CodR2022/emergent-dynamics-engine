import numpy as np


class EquationEngine:
    """
    Executable equation layer.

    This turns the equation into a modular command layer.

    Conceptual equation:

        du/dt =
            attraction
          + repulsion
          + nonlinear amplification
          + delayed communication
          + optional custom terms

    Discrete form:

        next_state = state + sum(term(state, delayed, strength, params))

    Each term is a callable with signature:

        term(state, delayed, strength, params) -> ndarray
    """

    def __init__(self, terms):
        self.terms = list(terms)

    def add_term(self, term):
        self.terms.append(term)

    def remove_term(self, term_name: str):
        self.terms = [
            term for term in self.terms
            if getattr(term, "__name__", "") != term_name
        ]

    def evaluate(self, state, delayed, strength, params):
        total = np.zeros_like(state, dtype=float)

        for term in self.terms:
            total += term(state, delayed, strength, params)

        return state + total

    def describe(self):
        return [getattr(term, "__name__", str(term)) for term in self.terms]
