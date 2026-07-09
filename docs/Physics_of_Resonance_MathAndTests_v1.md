# Mathematical Framework and Experimental Predictions

## Author

Maksym Marnov (Alchimist)

## Project

POSITRON–ISKORKA

## License

CC BY 4.0

## Mathematical Formulation

### Collective Phase Coherence

For N phase-bearing elements:

Z(t) = (1 / N) Σ_j exp(i θ_j(t))

The collective phase coherence magnitude is:

R(t) = |Z(t)|

with:

0 ≤ R(t) ≤ 1

The mean collective phase is:

φ(t) = arg Z(t)

R(t) → 1 indicates strong collective phase coherence.

R(t) → 0 indicates strong phase dispersion.

The complex order parameter therefore provides a direct measurable relation between the individual phase states θ_j(t), the collective phase φ(t), and the magnitude R(t) of collective phase coherence.

### Coupled RPU Phase Dynamics

The continuous phase dynamics of node i are represented by:

dθ_i / dt = ω_i + K Σ_j W_ij sin(θ_j - θ_i - γ) + A_i(t) sin(φ_i^ext - θ_i)

where:

- θ_i is the phase of node i;
- ω_i is its intrinsic angular frequency;
- K is the global coupling strength;
- W_ij is the coupling matrix;
- γ is the asymmetric phase-lag parameter;
- A_i(t) is the time-dependent external drive amplitude;
- φ_i^ext is the external drive phase.

The resulting evolution depends on the combined relation between intrinsic frequency, coupling topology, relative phase, asymmetric phase lag, external drive, modulation, perturbation, retention, and dissipation.

The process logic is:

interaction → relative phase dynamics → phase coherence or decoherence → dynamic retention or dissipation → transition boundary → branch selection → path dependence → inherited next state

### Transition Candidate

For a response curve R(α) across a continuously varied profile parameter α, the implemented transition diagnostic identifies the strongest local response gradient:

α* = arg max_α |dR / dα|

where α* is the extracted transition candidate.

A transition candidate is therefore associated with the region in which the collective response changes most strongly with respect to the scanned parameter.

The computational qualification layer tests the stability of α* under scan refinement and small controlled perturbations.

### Path Dependence and Hysteresis

The same parameter interval can be traversed in two directions:

forward: α = 0 → 1

reverse: α = 1 → 0

The resulting response branches are:

R_forward(α)

R_reverse(α)

The branch separation is:

ΔR(α) = |R_forward(α) - R_reverse(α)|

The integrated hysteresis measure is:

H = ∫_0^1 ΔR(α) dα

When H > 0, the observable response depends on the path by which the current parameter value was reached.

The process sequence is:

asymmetry → different trajectories → branch separation → transition boundary → hysteresis → dependence on prior state

### Local Jacobian and Spectral Structure

For a dynamical system:

dx / dt = F(x)

the local Jacobian is:

J_ij = ∂F_i / ∂x_j

The eigenvalues λ_k(J) describe the local dynamical directions around the current state.

The spectral abscissa is:

α(J) = max_k Re λ_k(J)

A negative real part corresponds to a locally decaying mode.

A zero or near-zero real part can indicate a neutral direction.

A positive real part can indicate local growth away from the current state.

For the coupling-only global phase direction:

J · 1 = 0

This relation expresses the neutral mode associated with a common rotation of all phases.

### Bloch State Admissibility

For the Bloch state vector:

s = (s_x, s_y, s_z)

the admissible state domain is:

s_x² + s_y² + s_z² ≤ 1

The corresponding two-level density matrix is:

ρ = 1/2 [[1 + s_z, s_x - i s_y], [s_x + i s_y, 1 - s_z]]

An admissible state satisfies:

ρ = ρ†

Tr(ρ) = 1

eigenvalues(ρ) ≥ 0

These conditions connect the geometric Bloch-state domain with the algebraic admissibility of the corresponding density matrix.

### Quantization

E = h f

Energy is stored in discrete resonance modes; Planck’s constant defines the minimal phase action.

### Schrödinger Equation — Resonant Form

(ħ² / 2m) ∇²ψ + Uψ = iħ ∂ψ / ∂t

Interpretation: collapse of ψ corresponds to phase-lock between the wave and observer contour.

### Gravitational Retention

r_s = 2GM / c²

Curvature arises where local resonance density reaches critical phase tension.

### Thermodynamics and Resonance Conservation

E_total = Σ_i E_i = const

E_i = 1/2 kA_i² = h f_i

Energy is not “lost”; it redistributes among coherent modes maintaining global resonance balance. Entropy increase reflects phase decoherence, not disappearance of energy.

### Disk Instability — Toomre Q

Q = c_s κ / (π G Σ)

Instability develops when Q < 1, leading to resonant clustering and structure formation.

### Hawking–Bekenstein Relation

S = k_B c³ A / (4 G ħ)

T_H = ħ c³ / (8π G M k_B)

## Experimental and Observational Predictions

### 1. Quantum Tunneling

Phase synchronization across a potential barrier creates “instantaneous” transmission — tunneling is resonance continuity, not mass transfer.

### 2. Cold Plasma Stability

Multi-frequency phase-locked excitation should maintain plasma without heating. Criterion of success — narrow spectral noise band and absence of phase slips.

### 3. Neutron Star Mergers

Phase realignment during collision explains heavy element synthesis (r-process).

Frequency invariant:

f_ISCO ≈ 2200 Hz × M_☉ / M

### 4. Saturn Hexagon

Standing-wave polygon in polar jet stream — stable phase-lock resonance around 6th harmonic.

### 5. Void of Boötes

Large-scale phase-defocused region — an anti-node of cosmological resonance lattice; bright filaments form at its phase-locked perimeter.

## Conclusion

Energy, structure, and spacetime themselves emerge from resonance coherence. When phases align, geometry appears; when coherence breaks, matter and fields disperse.

## Citation

Marnov, Maksym (Alchimist). (2025). Physics of Resonance: From Singularity to Event Horizon. POSITRON–ISKORKA Project, Berlin.
