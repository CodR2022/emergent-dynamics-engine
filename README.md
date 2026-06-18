# Emergent System Simulation

A modular Python simulation for exploring how structure, motion, persistence, and collapse can emerge from layered feedback rules.

The project integrates:

- local attraction / diffusion
- repulsion / anti-collapse spacing
- nonlinear amplification
- entropy / instability
- finite propagation speed / delayed communication
- an executable equation layer

## Core Idea

The system is not built from predefined objects.

It starts as a field of values.

Structure emerges from:

```text
interaction + opposition + delay
```

Conceptual form:

```text
du/dt =
    attraction
  + repulsion
  + nonlinear amplification
  + delayed communication
  + entropy / instability
```

Compact mathematical expression:

```text
du/dt = alpha * Laplacian(u_delay)
      - beta  * BiLaplacian(u_delay)
      + gamma * f(u)
      - delta * (u - u_delay)
      + noise/collapse
```

## Install

```bash
pip install -r requirements.txt
```

## Run

From the project root:

```bash
python -m examples.run_simulation
```

Do not run files from inside the package directly if they use package imports.

## Compare Modes

```bash
python -m examples.compare_modes
```

## Outputs

Generated plots are saved to:

```text
outputs/
```

## Conceptual Mapping

| Module term | Interpretation |
|---|---|
| diffusion | attraction / coherence |
| repulsion | spacing / anti-collapse |
| nonlinear amplification | self-reinforcing structure |
| delay | finite propagation / speed-of-light-like constraint |
| entropy noise | disturbance / decay pressure |
| collapse | instability / transmutation |
| strength | stabilized behavior becoming structure |

## Execution Layer

The equation is not hardcoded into the simulation loop.

The equation is a command layer:

```python
engine = EquationEngine([
    terms.diffusion_term,
    terms.repulsion_term,
    terms.nonlinear_amplification_term,
    terms.delay_term,
])
```

This means you can swap the laws without rewriting the engine.

## Notes

This is not a proof of physical reality.

It is a minimal experimental framework showing that structure-like, field-like, and motion-like behavior can emerge from simple layered rules.


A modular Python simulation for exploring how structure, motion, persistence, and collapse can emerge from layered feedback rules.

The project integrates:

- local attraction / diffusion
- repulsion / anti-collapse spacing
- nonlinear amplification
- entropy / instability
- finite propagation speed / delayed communication
- an executable equation layer

## Core Idea

The system is not built from predefined objects.

It starts as a field of values.

Structure emerges from:

```text
interaction + opposition + delay
```

Conceptual form:

```text
du/dt =
    attraction
  + repulsion
  + nonlinear amplification
  + delayed communication
  + entropy / instability
```

Compact mathematical expression:

```text
du/dt = alpha * Laplacian(u_delay)
      - beta  * BiLaplacian(u_delay)
      + gamma * f(u)
      - delta * (u - u_delay)
      + noise/collapse
```

## Install

```bash
pip install -r requirements.txt
```

## Run

From the project root:

```bash
python -m examples.run_simulation
```

Do not run files from inside the package directly if they use package imports.

## Compare Modes

```bash
python -m examples.compare_modes
```

## Outputs

Generated plots are saved to:

```text
outputs/
```

## Conceptual Mapping

| Module term | Interpretation |
|---|---|
| diffusion | attraction / coherence |
| repulsion | spacing / anti-collapse |
| nonlinear amplification | self-reinforcing structure |
| delay | finite propagation / speed-of-light-like constraint |
| entropy noise | disturbance / decay pressure |
| collapse | instability / transmutation |
| strength | stabilized behavior becoming structure |

## Execution Layer

The equation is not hardcoded into the simulation loop.

The equation is a command layer:

```python
engine = EquationEngine([
    terms.diffusion_term,
    terms.repulsion_term,
    terms.nonlinear_amplification_term,
    terms.delay_term,
])
```

This means you can swap the laws without rewriting the engine.

## Notes

This is not a proof of physical reality.

It is a minimal experimental framework showing that structure-like, field-like, and motion-like behavior can emerge from simple layered rules.
