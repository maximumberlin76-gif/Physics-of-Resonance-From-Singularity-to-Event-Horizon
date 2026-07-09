# Physics of Resonance — From Singularity to Event Horizon

[![Resonance Core Validation](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-core-validation.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-core-validation.yml)
[![Python Compatibility](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-python-compatibility.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-python-compatibility.yml)
[![Numerical Accuracy and Convergence](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-numerical-accuracy-convergence.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-numerical-accuracy-convergence.yml)
[![Stress and Scaling](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-stress-scaling.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-stress-scaling.yml)
[![Edge Cases and Failure Modes](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-edge-cases-failure-modes.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-edge-cases-failure-modes.yml)
[![Determinism and Reproducibility](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-determinism-reproducibility.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-determinism-reproducibility.yml)
[![Structural Invariants and Metamorphic Relations](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-structural-invariants-metamorphic-relations.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-structural-invariants-metamorphic-relations.yml)
[![Perturbation Robustness and Sensitivity](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-perturbation-robustness-sensitivity.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-perturbation-robustness-sensitivity.yml)
[![Physical State Admissibility and Domain Bounds](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-physical-state-admissibility-domain-bounds.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-physical-state-admissibility-domain-bounds.yml)
[![Bifurcation Transition Boundaries and Hysteresis](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-bifurcation-transition-hysteresis.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-bifurcation-transition-hysteresis.yml)
[![Spectral Stability and Local Dynamics](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-spectral-stability-local-dynamics.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-spectral-stability-local-dynamics.yml)

## Resonance as an Observable Mechanism of Structural Self-Organization

**Physics of Resonance — From Singularity to Event Horizon** presents resonance as an effective observable mechanism of structural self-organization of Matter, Space, and Time.

The repository develops this mechanism through coupled phase dynamics, phase coherence and decoherence, dissipation, asymmetric interaction, perturbation response, transition boundaries, path dependence, hysteresis, bifurcation candidates, and local spectral structure.

The theoretical description is connected directly to executable numerical implementations. The repository contains an executable RPU resonant core, a deterministic dissipative Bloch trajectory layer, analytical stationary-state calculation, numerical integration, parameter scans, perturbation analysis, transition-path continuation, Jacobian reconstruction, local spectral analysis, and an eleven-workflow GitHub Actions qualification ladder.

The broader theoretical framework examines resonance-based interpretations of quantization, gravitational retention, tunneling, plasma stability, astrophysical structure, and scale-dependent phase coherence.

Part of the **POSITRON–ISKORKA Project**.

---

## Core Process Logic

The repository treats observable structure as the dynamic result of coupled open-system evolution rather than as a static arrangement.

**interaction → relative phase dynamics → phase coherence or decoherence → dynamic retention or dissipation → transition boundary → branch selection → path dependence → inherited next state**

Coupled phase-bearing elements continuously modify one another through their relative phases and interaction strengths. Constructive phase relations can support collective coherence, while detuning, dissipation, perturbation, asymmetric phase lag, coupling topology, and external drive can weaken, redirect, or reorganize that coherence.

When coherence is dynamically retained, a collective state can persist over time. When the dynamical balance changes, the system can leave the previous regime, cross a transition boundary, and enter another branch of evolution.

The resulting state can depend not only on the current parameter values but also on the trajectory by which those values were reached. Forward and reverse parameter paths can therefore produce different responses.

**asymmetry → different trajectories → branch separation → transition boundary → hysteresis → dependence on prior state**

Local Jacobian and spectral analysis describe the immediate geometry of evolution around a given state: whether small perturbations decay, persist as neutral directions, or grow toward another dynamical regime.

---

## Mathematical Core

### Collective Phase Coherence

For `N` phase-bearing elements:

`Z(t) = (1 / N) Σ_j exp(i θ_j(t))`

The collective phase coherence magnitude is:

`R(t) = |Z(t)|`

with:

`0 ≤ R(t) ≤ 1`

`R(t) → 1` indicates strong collective phase coherence.

`R(t) → 0` indicates strong phase dispersion.

The mean collective phase is:

`φ(t) = arg Z(t)`

The executable qualification layer verifies that the measured coherence remains inside its admissible interval and that the collective phase remains finite.

### RPU Coupled Phase Dynamics

The continuous phase component implemented by the RPU core follows the structure:

`dθ_i / dt = ω_i + K Σ_j W_ij sin(θ_j - θ_i - γ) + A_i(t) sin(φ_i^ext - θ_i)`

where:

- `θ_i` is the phase of node `i`;
- `ω_i` is its intrinsic angular frequency;
- `K` is the global coupling strength;
- `W_ij` is the coupling matrix;
- `γ` is the asymmetric phase-lag parameter;
- `A_i(t)` is the time-dependent external drive amplitude;
- `φ_i^ext` is the external drive phase.

The implemented dynamics additionally include:

- deterministic frequency-profile locking;
- deterministic amplitude-profile locking;
- amplitude modulation;
- frequency modulation;
- optional stochastic perturbation;
- anti-lock response;
- structured imprinting into the coupling matrix;
- balanced ternary state control;
- persistent quantized coupling weights;
- scan-mode interpolation between resonance profiles.

The resulting dynamics arise from the evolving relation between:

**intrinsic frequency + coupling topology + relative phase + asymmetric phase lag + external drive + modulation + perturbation + retention and dissipation**

### Balanced Ternary State Layer

The discrete control layer uses:

`s_i ∈ {-1, 0, 1}`

and:

`W_ij^q ∈ {-1, 0, 1}`

The ternary states are generated by balanced threshold quantization. The qualification ladder verifies that the state vector and the quantized coupling matrix remain inside the balanced ternary domain during initialization, imprinting, deterministic evolution, perturbation analysis, long-duration execution, and stress workloads.

This creates a coupled architecture in which continuous phase dynamics and discrete ternary control evolve together.

### Dissipative Bloch Dynamics

The repository implements the driven dissipative Bloch system:

`ds_x / dt = -s_x / T2 + Δ s_y`

`ds_y / dt = -s_y / T2 - Δ s_x + Ω s_z`

`ds_z / dt = -(s_z + 1) / T1 - Ω s_y`

with:

`T1 = 1 / γ`

`T2 = 2 T1`

where:

- `Ω` is the coherent drive frequency;
- `γ` is the dissipation rate;
- `Δ` is the detuning;
- `(s_x, s_y, s_z)` is the Bloch state vector.

The admissible state domain is:

`s_x² + s_y² + s_z² ≤ 1`

The implementation includes analytical stationary-state calculation, fixed-step fourth-order Runge–Kutta integration, deterministic multi-ratio trajectory generation, CSV export, graphical rendering, perturbation recovery analysis, Jacobian analysis, and spectral stability analysis.

---

## Two Complementary Executable Layers

### RPU Resonant Core

The RPU layer models:

**collective nonlinear phase evolution + asymmetric coupling + external resonance profiles + modulation + perturbation + balanced ternary control**

Its primary object is the evolution of a coupled population of phase-bearing nodes.

### Dissipative Bloch Layer

The Bloch layer models:

**local driven dissipative state evolution + analytical stationary states + numerical integration + admissible state-domain analysis**

Its primary object is the evolution of a driven dissipative three-component state.

The shared object of analysis is:

**emergence → retention → perturbation → loss → transition → inheritance**

of dynamically coherent states.

---

## Dynamic Asymmetry, Transition, and Hysteresis

The RPU interaction includes an explicit asymmetric phase lag:

`γ ≠ 0`

The coupling term therefore depends on:

`θ_j - θ_i - γ`

rather than on idealized symmetric phase alignment alone.

For a response curve `R(α)` across a continuously varied profile parameter `α`, the implemented transition workflow extracts reproducible transition candidates from the strongest local change of the response curve and tests their stability under scan refinement and small drive perturbations.

The same parameter interval is then traversed in two directions:

**forward: α = 0 → 1**

**reverse: α = 1 → 0**

The resulting branches are compared as `R_forward(α)` and `R_reverse(α)`.

The branch separation is:

`ΔR(α) = |R_forward(α) - R_reverse(α)|`

The integrated hysteresis measure is:

`H = ∫ ΔR(α) dα`

The qualification layer verifies deterministic transition-candidate extraction, finite branch separation, finite hysteresis area, and reproducibility of forward and reverse paths.

This makes the history of the system part of the observable dynamical response.

---

## Local Dynamics and Spectral Structure

For a dynamical system:

`dx / dt = F(x)`

the local Jacobian is:

`J_ij = ∂F_i / ∂x_j`

The eigenvalues of `J` describe local dynamical directions. The spectral abscissa is:

`α(J) = max Re λ_k(J)`

A negative real part corresponds to a locally decaying mode.

A zero or near-zero real part can indicate a neutral direction.

A positive real part can indicate local growth away from the current state.

The qualification layer verifies:

- analytical and numerical Bloch Jacobian agreement;
- negative spectral abscissa across the tested dissipative Bloch parameter domain;
- analytical and numerical RPU Jacobian agreement;
- second-order centered finite-difference Jacobian refinement;
- the global phase neutral mode of the coupling-only RPU system;
- quadratic scaling of the nonlinear remainder around local linearization;
- deterministic change of the local RPU spectral marker under resonance-profile morphing.

For the coupling-only global phase direction:

`J · 1 = 0`

This corresponds to invariance under a common rotation of all phases.

---

## Structural Invariants and State Domains

The repository verifies that mathematically equivalent representations remain dynamically equivalent.

### Global Phase Rotation

`θ_i → θ_i + δ`

The collective coherence magnitude remains invariant while the collective phase shifts by the same amount.

### Full-Turn Phase Equivalence

`θ_i → θ_i + 2π n_i`

for integer `n_i`.

Equivalent angular representations evolve to equivalent states.

### Node Relabeling

A consistent permutation of phases, intrinsic frequencies, external profiles, coupling matrices, and ternary states preserves the collective dynamics.

### Balanced Ternary Reflection

`Q(-x) = -Q(x)`

within the defined threshold structure.

### Bloch State Domain

`s_x² + s_y² + s_z² ≤ 1`

The corresponding two-level density matrix is reconstructed as:

`ρ = 1/2 [[1 + s_z, s_x - i s_y], [s_x + i s_y, 1 - s_z]]`

The qualification layer verifies:

`ρ = ρ†`

`Tr(ρ) = 1`

`eigenvalues(ρ) ≥ 0`

within numerical tolerance.

### RPU State Domain

`0 ≤ θ_i < 2π`

`0 ≤ φ_i^ext < 2π`

`0 ≤ R ≤ 1`

`s_i ∈ {-1, 0, 1}`

`W_ij^q ∈ {-1, 0, 1}`

The computational apparatus is therefore tested not only for execution but also for closure inside its defined state spaces.

---

## Numerical Methods

### RPU Integration

The RPU continuous phase state is advanced through a two-evaluation predictor-corrector structure. The implementation supports an optional stability guard that reduces the timestep under sufficiently strong finite drive.

### Bloch Integration

The Bloch trajectory layer uses fixed-step fourth-order Runge–Kutta integration. The qualification ladder verifies monotonic error decrease under timestep refinement, observed fourth-order convergence, long-time convergence toward the analytical stationary state, and CSV numerical fidelity.

### Stationary-State Analysis

The Bloch stationary state is obtained by solving:

`ds_x / dt = 0`

`ds_y / dt = 0`

`ds_z / dt = 0`

The resulting state is substituted back into the dynamical equations and validated through the residual norm.

---

## Executable Architecture

### Public RPU API

- `RPUCore`
- `power_iteration_radius`
- `quantize_balanced`
- `quantize_W`

### RPU Core

File: `rpu_core/rpu_core_v1.py`

Provides coupled phase evolution, asymmetric phase-lag interaction, external frequency and amplitude locking, deterministic seeded execution, structured imprinting, balanced ternary control, modulation, anti-lock response, collective order-parameter measurement, cluster measurement, scan-mode execution, and transition-candidate diagnostics.

### Dissipative Bloch Trajectory Generator

File: `rpu_core/twa_demo/run_twa_demo.py`

Provides validated parameter handling, the dissipative Bloch vector field, fixed-step RK4 integration, analytical stationary states, deterministic multi-ratio trajectory generation, and CSV artifact generation.

### Trajectory Plotter

File: `plot_twa_results.py`

Provides CSV trajectory discovery, required-column validation, finite-value validation, strictly increasing time validation, trajectory-set validation, headless plotting, and PNG artifact generation.

---

## Quick Start

### Requirements

Supported Python versions:

- Python 3.10
- Python 3.11
- Python 3.12

Install runtime dependencies:

`python -m pip install numpy matplotlib`

Run the RPU core:

`python rpu_core/rpu_core_v1.py`

Run the RPU scan path:

`python rpu_core/rpu_core_v1.py --scan`

Generate dissipative Bloch trajectories:

`python rpu_core/twa_demo/run_twa_demo.py`

Default trajectory ratios:

- `γ / Ω = 0.1`
- `γ / Ω = 0.2`
- `γ / Ω = 0.5`
- `γ / Ω = 1.0`

Default output directory:

`rpu_core/twa_demo/logs/`

Render the Bloch plot:

`python plot_twa_results.py --no-show`

Default plot output:

`rpu_core/twa_demo/logs/bloch_twa_results.png`

---

## Computational Qualification Ladder

The repository uses eleven GitHub Actions workflows.

### 1. Resonance Core Validation

Validates the executable core path, public API, standard and scan execution, external drive response, deterministic replay, invalid profile rejection, Bloch CSV generation, PNG rendering, and repository integrity.

### 2. Resonance Python Compatibility

Validates the executable path on Python 3.10, 3.11, and 3.12.

### 3. Resonance Numerical Accuracy and Convergence

Validates analytical stationary-state residuals, fourth-order RK4 refinement, long-time Bloch convergence, RPU timestep refinement, and CSV numerical fidelity.

### 4. Resonance Stress and Scaling

Validates increasing RPU node count, long-duration execution, diverse resonance profiles, large Bloch trajectory batches, and finite states under load.

### 5. Resonance Edge Cases and Failure Modes

Validates invalid numerical inputs, constructor rejection paths, profile-shape errors, non-finite input rejection, state preservation after rejected operations, extreme finite drive handling, corrupted CSV rejection, and failure isolation.

### 6. Resonance Determinism and Reproducibility

Validates exact seeded replay, chunk-boundary invariance, deterministic seed separation, independent-process reproducibility, byte-identical Bloch CSV generation, and deterministic plot raster.

### 7. Resonance Structural Invariants and Metamorphic Relations

Validates balanced ternary reflection, coupling and state structure, full-turn phase equivalence, global phase covariance, node-relabeling covariance, Bloch stationary fixed points, and autonomous time-translation invariance.

### 8. Resonance Perturbation Robustness and Sensitivity

Validates initial phase perturbation scaling, frequency-profile sensitivity, amplitude-profile sensitivity, finite-difference sensitivity convergence, Bloch perturbation linearity and superposition, and dissipative recovery.

### 9. Resonance Physical State Admissibility and Domain Bounds

Validates Bloch unit-ball preservation, density-matrix Hermiticity, unit trace, positive-semidefinite state domain, generated CSV state admissibility, compact RPU phase domains, and balanced ternary domain closure.

### 10. Resonance Bifurcation Transition Boundaries and Hysteresis

Validates deterministic transition-candidate extraction, stability under scan refinement, stability under small drive perturbation, forward and reverse continuation branches, finite branch separation, finite hysteresis area, and a path-independent Bloch stationary control.

### 11. Resonance Spectral Stability and Local Dynamics

Validates analytical and numerical Jacobian agreement, dissipative Bloch spectral stability, RPU Jacobian refinement, the global phase neutral mode, nonlinear linearization order, and local spectral response to resonance-profile morphing.

### Qualification Logic

**execution → compatibility → numerical convergence → stress and scaling → controlled failure → determinism → structural invariance → perturbation sensitivity → state admissibility → transition and hysteresis → local spectral structure**

Each layer tests a different property of the implemented apparatus.

---

## Theoretical Scope

The documents in `docs/` develop the broader resonance framework across multiple physical domains.

Topics include:

- quantization and stable resonance modes;
- phase closure and boundary conditions;
- gravitational retention;
- thermodynamic redistribution and decoherence;
- disk instability and accretion;
- event horizons;
- quantum tunneling;
- plasma stability;
- neutron-star mergers;
- astrophysical structures;
- large-scale coherence and dephasing.

The repository connects these theoretical discussions to executable models of:

**phase interaction → coherence → dissipation → perturbation → transition → retention → path dependence → local stability**

The GitHub Actions qualification ladder validates the computational properties of the implemented apparatus.

---

## Repository Structure

- `.github/workflows/` — eleven computational qualification workflows
- `docs/Physics_of_Resonance_WhitePaper_v1.md` — broader theoretical framework
- `docs/Physics_of_Resonance_MathAndTests_v1.md` — mathematical formulation and prediction layer
- `rpu_core/__init__.py` — public package API
- `rpu_core/rpu_core_v1.py` — RPU resonant core
- `rpu_core/twa_demo/run_twa_demo.py` — deterministic dissipative Bloch trajectory generator
- `plot_twa_results.py` — validated trajectory plotting pipeline
- `LICENSE_CODE` — Apache License 2.0 for code
- `README.md` — repository overview and execution guide

---

## Documentation

### White Paper

`docs/Physics_of_Resonance_WhitePaper_v1.md`

Contains the broader theoretical framework from the singularity point to the event horizon.

### Mathematical Framework and Experimental Predictions

`docs/Physics_of_Resonance_MathAndTests_v1.md`

Contains the mathematical formulation and the experimental or observational prediction layer.

---

## Licenses

### Code

Apache License 2.0.

See `LICENSE_CODE`.

### Documentation

Creative Commons Attribution 4.0 International, as declared in the project documentation.

---

## Citation

Marnov, Maksym (Alchimist). (2025). *Physics of Resonance: From Singularity to Event Horizon*. POSITRON–ISKORKA Project, Berlin.

---

## Author

**Maksym Marnov (Alchimist)**

**POSITRON–ISKORKA Project**

Berlin
