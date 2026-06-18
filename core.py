"""
Emergent System Simulation

A modular simulation framework for exploring:
- attraction / diffusion
- repulsion / anti-diffusion
- nonlinear amplification
- entropy / noise / collapse
- finite propagation speed / delayed communication
- layered execution rules

Core idea:
    structure emerges from interaction + opposition + delay.
"""

from .params import Params
from .simulation import Simulation
from .execution import EquationEngine
