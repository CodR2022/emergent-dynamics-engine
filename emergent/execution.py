from __future__ import annotations

from collections.abc import Callable
from typing import Any

import numpy as np


TermFunction = Callable[
    [np.ndarray, np.ndarray, np.ndarray, Any],
    np.ndarray,
]


class EquationEngine:
    """
    Executes a list of equation terms.

    Each term receives:

        state
        delayed
        strength
        params

    and returns a grid-shaped update.

    The engine adds all term outputs together and applies them to the current state.
    """

    def __init__(self, terms: list[TermFunction] | None = None):
        self.terms: list[TermFunction] = list(terms or [])

    def add_term(self, term: TermFunction) -> None:
        """
        Add a new equation term.
        """
        self.terms.append(term)

    def remove_term(self, term_name: str) -> None:
        """
        Remove a term by function name.
        """
        self.terms = [
            term for term in self.terms
            if getattr(term, "__name__", "") != term_name
        ]

    def evaluate(
        self,
        state: np.ndarray,
        delayed: np.ndarray,
        strength: np.ndarray,
        params: Any,
    ) -> np.ndarray:
        """
        Evaluate one full equation step.
        """
        update = np.zeros_like(state, dtype=float)

        for term in self.terms:
            update += term(state, delayed, strength, params)

        return state + update

    def describe(self) -> list[str]:
        """
        Return the active equation term names.
        """
        return [
            getattr(term, "__name__", str(term))
            for term in self.terms
        ]
