# Continuous Integration and Qualification

This document is the public index of the continuous-integration and executable qualification layer for:

**Physics of Resonance: From the Singularity Point to the Event Horizon**

The repository uses eleven GitHub Actions workflows to test the executable numerical implementation across:

- core execution;
- Python compatibility;
- numerical accuracy and convergence;
- stress and scaling behavior;
- edge cases and failure modes;
- determinism and reproducibility;
- structural invariants and metamorphic relations;
- perturbation robustness and sensitivity;
- physical state admissibility and domain bounds;
- bifurcation, transition, and hysteresis behavior;
- local Jacobian and spectral stability.

The workflows are intended to test the implementation as executable software and numerical dynamics.

They do not replace experimental validation of physical hypotheses.

---

## Qualification Status

[![Resonance Core Validation](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-core-validation.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-core-validation.yml)

[![Resonance Python Compatibility](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-python-compatibility.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-python-compatibility.yml)

[![Resonance Numerical Accuracy and Convergence](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-numerical-accuracy-convergence.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-numerical-accuracy-convergence.yml)

[![Resonance Stress and Scaling](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-stress-scaling.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-stress-scaling.yml)

[![Resonance Edge Cases and Failure Modes](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-edge-cases-failure-modes.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-edge-cases-failure-modes.yml)

[![Resonance Determinism and Reproducibility](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-determinism-reproducibility.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-determinism-reproducibility.yml)

[![Resonance Structural Invariants and Metamorphic Relations](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-structural-invariants-metamorphic-relations.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-structural-invariants-metamorphic-relations.yml)

[![Resonance Perturbation Robustness and Sensitivity](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-perturbation-robustness-sensitivity.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-perturbation-robustness-sensitivity.yml)

[![Resonance Physical State Admissibility and Domain Bounds](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-physical-state-admissibility-domain-bounds.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-physical-state-admissibility-domain-bounds.yml)

[![Resonance Bifurcation Transition and Hysteresis](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-bifurcation-transition-hysteresis.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-bifurcation-transition-hysteresis.yml)

[![Resonance Spectral Stability and Local Dynamics](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-spectral-stability-local-dynamics.yml/badge.svg)](https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions/workflows/resonance-spectral-stability-local-dynamics.yml)

The badges above report the live GitHub Actions status of the corresponding workflows.

---

## Qualification Matrix

| # | Workflow | Qualification Layer |
|---|---|---|
| 1 | `resonance-core-validation.yml` | Core executable behavior |
| 2 | `resonance-python-compatibility.yml` | Supported Python execution compatibility |
| 3 | `resonance-numerical-accuracy-convergence.yml` | Numerical accuracy and refinement behavior |
| 4 | `resonance-stress-scaling.yml` | Stress conditions and scaling behavior |
| 5 | `resonance-edge-cases-failure-modes.yml` | Edge cases and controlled failure behavior |
| 6 | `resonance-determinism-reproducibility.yml` | Determinism and reproducible execution |
| 7 | `resonance-structural-invariants-metamorphic-relations.yml` | Structural invariants and equivalent transformations |
| 8 | `resonance-perturbation-robustness-sensitivity.yml` | Perturbation response and sensitivity |
| 9 | `resonance-physical-state-admissibility-domain-bounds.yml` | Physical and numerical state-domain closure |
| 10 | `resonance-bifurcation-transition-hysteresis.yml` | Transition boundaries, branch structure, and hysteresis |
| 11 | `resonance-spectral-stability-local-dynamics.yml` | Local Jacobians, eigenvalues, and spectral response |

---

## 1. Core Validation

Workflow:

`resonance-core-validation.yml`

Purpose:

Validate the principal executable paths of the repository before deeper qualification layers are applied.

The workflow acts as the first integration gate for the implementation.

It checks that the tested core components can execute under the repository configuration and produce structurally valid outputs.

The core layer includes the executable phase-dynamics and state-processing path used by later workflows.

A failure at this level indicates that higher-order qualification results should not be treated as valid until the core execution problem is resolved.

---

## 2. Python Compatibility

Workflow:

`resonance-python-compatibility.yml`

Purpose:

Test the executable repository against the Python environments defined by the workflow.

The workflow is intended to detect:

- unsupported syntax;
- import failures;
- runtime incompatibilities;
- environment-dependent execution errors.

Compatibility qualification is kept separate from physical and numerical qualification.

A program can be numerically correct in one environment and still fail as a portable software implementation.

---

## 3. Numerical Accuracy and Convergence

Workflow:

`resonance-numerical-accuracy-convergence.yml`

Purpose:

Test whether numerical results behave consistently under controlled refinement.

Relevant checks can include comparison across:

- integration timesteps;
- numerical resolutions;
- refinement levels;
- independent formulations of the same quantity.

The central principle is:

**numerical result → controlled refinement → convergence or bounded numerical error**

A result that changes without control under numerical refinement is not treated as numerically qualified.

---

## 4. Stress and Scaling

Workflow:

`resonance-stress-scaling.yml`

Purpose:

Test executable behavior beyond the smallest reference configurations.

The workflow examines whether the implementation remains controlled as the tested problem size or workload increases.

The qualification target is not unlimited scalability.

It is controlled behavior across the stress and scaling ranges explicitly defined by the workflow.

Relevant failure classes include:

- non-finite values;
- uncontrolled runtime failure;
- broken state structure;
- scaling-dependent numerical corruption.

---

## 5. Edge Cases and Failure Modes

Workflow:

`resonance-edge-cases-failure-modes.yml`

Purpose:

Test states and parameters near the boundaries of normal operation.

The workflow is intended to distinguish:

- valid boundary behavior;
- explicitly rejected input;
- controlled failure;
- silent corruption.

Edge-case qualification is important because a model that behaves correctly only near one nominal parameter set is not sufficiently characterized.

The expected behavior must be explicit:

**valid input → valid result**

or:

**invalid input → controlled rejection**

Silent transition into an undefined numerical state is treated as failure.

---

## 6. Determinism and Reproducibility

Workflow:

`resonance-determinism-reproducibility.yml`

Purpose:

Test whether equivalent executions reproduce equivalent outputs under the defined deterministic conditions.

The qualification layer includes checks for repository-level reproducibility properties such as:

- exact seeded replay;
- chunk-boundary invariance;
- independent-process reproducibility;
- byte-identical trajectory artifacts where required;
- deterministic plotting.

The central relation is:

**same implementation + same parameters + same initial state + same deterministic conditions → same qualified result**

Stochastic behavior, where introduced, must be tested through an explicitly defined seed and statistical protocol rather than being silently mixed with deterministic execution.

---

## 7. Structural Invariants and Metamorphic Relations

Workflow:

`resonance-structural-invariants-metamorphic-relations.yml`

Purpose:

Test whether mathematically equivalent transformations preserve the corresponding executable behavior.

Relevant structural relations include:

### Full-Turn Phase Equivalence

θ_i → θ_i + 2πn_i

### Global Phase Rotation

θ_i → θ_i + δ

for dynamics governed only by relative phase differences.

### Node Relabeling

A consistent permutation of all node-indexed quantities should preserve the corresponding physical result.

### Balanced Ternary Reflection

For the defined quantizer:

Q(−x) = −Q(x)

within the specified threshold structure.

Metamorphic testing does not require a separate analytical answer for every input.

It tests whether transformations that should preserve or predictably modify the result actually do so in the implementation.

---

## 8. Perturbation Robustness and Sensitivity

Workflow:

`resonance-perturbation-robustness-sensitivity.yml`

Purpose:

Test the response of the executable system to controlled changes in:

- initial conditions;
- parameters;
- state variables;
- external perturbations.

For a reference state:

X_reference(t)

and a perturbed state:

X_perturbed(t)

define:

ΔX(t) = X_perturbed(t) − X_reference(t)

The workflow examines whether the response is:

- finite;
- reproducible;
- locally ordered where expected;
- sensitive to parameter changes in a measurable way.

The qualification target is not universal insensitivity.

A physical dynamical system can be sensitive.

The requirement is that the sensitivity itself be measurable and numerically controlled.

---

## 9. Physical State Admissibility and Domain Bounds

Workflow:

`resonance-physical-state-admissibility-domain-bounds.yml`

Purpose:

Verify that executable trajectories remain inside the mathematical and physical state domains defined by the model.

For the phase and ternary RPU layer, relevant state conditions include:

0 ≤ θ_i < 2π

0 ≤ R ≤ 1

s_i ∈ {−1, 0, 1}

W_ij^q ∈ {−1, 0, 1}

For the Bloch layer, relevant admissibility conditions include:

s_x² + s_y² + s_z² ≤ 1

and the corresponding density-matrix conditions:

ρ = ρ†

Tr(ρ) = 1

eigenvalues(ρ) ≥ 0

within numerical tolerance.

The qualification principle is:

**numerical evolution must remain inside the state domain defined by the model**

A trajectory that leaves the admissible domain cannot be treated as a valid result without an explicit explanation of the violation.

---

## 10. Bifurcation, Transition, and Hysteresis

Workflow:

`resonance-bifurcation-transition-hysteresis.yml`

Purpose:

Test how the executable system changes under controlled parameter continuation.

For a control parameter:

α

and observable:

Y(α)

a transition candidate can be associated with:

α* = arg max_α |dY / dα|

The workflow examines forward and reverse continuation paths.

For:

Y_forward(α)

and:

Y_reverse(α)

define:

ΔY(α) = |Y_forward(α) − Y_reverse(α)|

The integrated hysteresis measure is:

H_Y = ∫ ΔY(α) dα

The qualification layer distinguishes:

- smooth response;
- strong transition region;
- branch separation;
- path dependence.

A transition candidate is treated as a numerical diagnostic.

It is not automatically a universal physical critical point.

---

## 11. Spectral Stability and Local Dynamics

Workflow:

`resonance-spectral-stability-local-dynamics.yml`

Purpose:

Test the local dynamical structure of the executable models through Jacobians, eigenvalues, and controlled linearization.

For:

dX / dt = F(X)

the local Jacobian is:

J_ij = ∂F_i / ∂X_j

For an eigenvalue:

λ_k = a_k + ib_k

the real part:

Re λ_k = a_k

determines local exponential growth or decay of the corresponding perturbation mode.

The spectral abscissa is:

α(J) = max_k Re λ_k(J)

The workflow qualifies:

- analytical and numerical Bloch Jacobians;
- dissipative spectral stability;
- RPU local Jacobian reconstruction;
- derivative-step refinement;
- the global phase neutral mode;
- nonlinear linearization order;
- deterministic spectral response to profile morphing.

For relative-phase coupling, a common global rotation:

θ_i → θ_i + δ

does not change internal phase differences.

The corresponding neutral direction satisfies:

J · 1 = 0

This zero mode represents global phase invariance.

It is not interpreted as an instability.

---

## Bloch-Layer Scope

The executable Bloch component is used as a deterministic dissipative trajectory and local-stability qualification layer.

It supports tests of:

- driven Bloch evolution;
- dissipation;
- stationary states;
- controlled perturbations;
- admissible Bloch-domain preservation;
- local Jacobians;
- spectral stability.

The current deterministic trajectory layer should not be described as a complete stochastic ensemble TWA implementation.

Its qualification claims are limited to the executable behavior actually tested by the repository.

---

## Qualification Logic

The eleven workflows form a layered qualification structure:

**core execution**

→ **environment compatibility**

→ **numerical convergence**

→ **stress and scaling**

→ **edge-case behavior**

→ **deterministic reproducibility**

→ **structural invariants**

→ **perturbation sensitivity**

→ **state-domain admissibility**

→ **transition and hysteresis structure**

→ **local spectral stability**

No single workflow is treated as sufficient by itself.

The repository combines independent test classes because different failure modes require different diagnostics.

---

## Evidence Rules

The CI layer distinguishes several forms of evidence.

### Software Evidence

A workflow can demonstrate that:

- code executes;
- outputs satisfy defined tests;
- deterministic runs reproduce;
- numerical invariants hold;
- state bounds are preserved.

### Numerical Evidence

A workflow can demonstrate that:

- refinement behavior is controlled;
- independent Jacobian estimates agree within tolerance;
- transition diagnostics are reproducible;
- perturbation response is measurable.

### Physical Interpretation

A successful workflow does not by itself establish that every physical interpretation in the White Paper is experimentally confirmed.

The executable layer tests the implemented mathematical and numerical structures.

Experimental and observational hypotheses require their own physical measurements and controls.

---

## Failure Interpretation

A failed workflow indicates that at least one defined qualification condition was not satisfied.

The correct response is:

**identify failing layer → inspect exact test → reproduce locally → correct implementation or test definition → rerun qualification**

A failure should not be hidden by weakening an acceptance threshold unless the revised threshold is independently justified.

---

## Reproducibility Record

For a computational result to be reproducible, the relevant execution record should identify:

- source revision;
- workflow definition;
- Python environment;
- dependencies;
- parameters;
- initial conditions;
- random seed where applicable;
- numerical timestep or resolution;
- acceptance thresholds.

GitHub Actions preserves the executable workflow history associated with repository revisions.

The workflow source remains the authoritative specification of the exact commands and acceptance criteria executed by CI.

---

## Public Qualification Boundary

The CI layer supports the following public claims:

- the repository contains executable Python reference implementations;
- the implementation is tested through eleven GitHub Actions qualification workflows;
- the qualification structure includes numerical, deterministic, invariant, perturbation, admissibility, transition, and spectral tests;
- workflow status is publicly inspectable through GitHub Actions.

The CI layer does not convert a numerical or software test into experimental validation of a physical hypothesis.

---

## Repository Links

- **Repository:** https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon
- **GitHub Actions:** https://github.com/maximumberlin76-gif/Physics-of-Resonance-From-Singularity-to-Event-Horizon/actions
- **White Paper:** `docs/Physics_of_Resonance_WhitePaper_v1.md`
- **Mathematical and Test Framework:** `docs/Physics_of_Resonance_MathAndTests_v1.md`
- **Citation:** `CITATION.md`

---

## Summary

The continuous-integration layer tests the executable framework through eleven independent qualification workflows.

The complete sequence is:

**execute → verify compatibility → refine numerically → stress → test failure boundaries → reproduce → preserve invariants → perturb → enforce admissibility → scan transitions → inspect local spectrum**

The purpose of the CI system is not to make claims by automation.

Its purpose is to expose the implementation to explicit, reproducible, and publicly inspectable qualification conditions.
