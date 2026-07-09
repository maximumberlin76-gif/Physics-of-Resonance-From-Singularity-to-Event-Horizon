PHYSICS OF RESONANCE: FROM THE SINGULARITY POINT TO THE EVENT HORIZON

Author

Maksym Marnov (Alchimist)

Project

POSITRON–ISKORKA

License

CC BY 4.0

Version

v1.0

## Abstract

We present a resonance–fractal framework in which resonance is treated as an effective observable mechanism of structural self-organization of Matter, Space, and Time.

The framework develops a continuous process logic through coupled phase dynamics, phase coherence and decoherence, dissipation, asymmetric interaction, dynamic retention, perturbation response, transition boundaries, branch selection, path dependence, hysteresis, and local spectral structure.

The theoretical layer examines resonance-based interpretations of quantization, gravitational retention, tunneling, plasma stability, astrophysical structure, and scale-dependent phase coherence.

The mathematical layer connects these interpretations to measurable dynamical quantities: the complex collective order parameter, phase coherence magnitude, asymmetric coupled-phase evolution, transition-candidate gradients, forward and reverse continuation branches, hysteresis area, local Jacobians, spectral abscissa, and admissible Bloch-state domains.

The executable layer includes the RPU resonant core and a deterministic dissipative Bloch trajectory model. The computational apparatus is qualified through numerical convergence, reproducibility, structural invariants, perturbation sensitivity, state admissibility, transition-boundary analysis, hysteresis, and local spectral dynamics.

The resulting framework follows the process sequence:

**interaction → relative phase dynamics → phase coherence or decoherence → dynamic retention or dissipation → transition boundary → branch selection → path dependence → inherited next state**

## Terms

**Resonant node:** a localized dynamically retained mode whose phase relations remain sufficiently coherent under the governing boundary conditions.

**Singularity point (O):** the minimal reference point of the framework from which boundary conditions, phase closure, and subsequent structural evolution are defined.

**Minimal form:** the triangle in two dimensions and the tetrahedron in three dimensions as the minimal closed geometries used in this framework. In three dimensions, the tetrahedral cell provides a non-coplanar closed configuration.

**Phase-lock (PL):** a bounded relative-phase relation maintained within a tolerance `Δφ` over a specified interval of evolution.

**Phase coherence:** the collective dynamical consistency of phase relations across an interacting population. In the executable layer it is measured through the complex order parameter `Z(t)` and its magnitude `R(t)`.

**Decoherence:** loss or dispersion of previously retained phase relations under detuning, dissipation, perturbation, noise, or changing interaction conditions.

**Fractal folding:** scale-dependent recurrence of structural relations, resonance ratios, or phase relations across hierarchical levels.

**Retention:** the persistence of a dynamically coherent state through continued interaction, energy redistribution, and dissipation. In the gravitational sections of this framework, retention is interpreted through the relation between localized energy and spacetime geometry.

**Asymmetric phase lag:** a non-zero phase offset `γ` in the interaction term `θ_j - θ_i - γ`, producing direction-dependent phase response and allowing different dynamical trajectories.

**Transition candidate:** a reproducible region of strongest local change in an observable response curve under controlled parameter variation.

**Branch selection:** entry into one of multiple dynamically distinguishable continuation paths after the system crosses or approaches a transition region.

**Path dependence:** dependence of the current observable state on the trajectory by which the current parameter values were reached.

**Hysteresis:** finite separation between forward and reverse continuation branches over the same parameter interval.

**Local Jacobian:** the matrix of first derivatives of the dynamical vector field around a given state, used to describe the local geometry of perturbation evolution.

**Local spectral structure:** the eigenvalue structure of the local Jacobian, describing locally decaying, neutral, or growing dynamical directions.

Fundamental Laws

## Law 1. Point-Source (δ)

### Statement

A localized source defines the boundary conditions of the field. Dynamically retained resonant nodes are stationary or locally persistent solutions compatible with those boundary conditions.

### Mathematical Form

Let:

L[Ψ] = J

with:

J(r) = J₀ δ(r − r₀)

and the corresponding boundary conditions.

For a Green’s function G satisfying:

L[G] = δ

the field is:

Ψ = G ∗ J

Stationary nodes correspond to extrema of the action S[Ψ] under variations that preserve the governing boundary conditions:

δS = 0

which yields the corresponding Euler–Lagrange equations.

### Phase Closure

For a closed stationary mode:

Δφ = 2πn

where n is an integer.

This condition expresses phase closure of the mode under the governing boundary conditions.

Phase closure alone does not determine dynamical retention. Persistence of the resulting state depends on its evolution under coupling, perturbation, dissipation, and local stability.

In the executable framework, these properties are examined through collective phase coherence, perturbation response, Jacobian reconstruction, and local spectral structure.

## Law 2. Minimal Form

### Statement

The minimal closed carrier is the triangle in two dimensions and the tetrahedron in three dimensions.

In three dimensions, the tetrahedron is the minimal non-coplanar closed geometry. Its four vertices and six edges provide the smallest framework that can constrain internal deformation while preserving the six global rigid-body modes of translation and rotation.

### Geometric Condition

For tetrahedral vertices r₁, r₂, r₃, and r₄, the signed volume is:

V_tet = (1 / 6) det[r₂ − r₁, r₃ − r₁, r₄ − r₁]

A non-degenerate tetrahedral cell requires:

V_tet ≠ 0

If:

V_tet = 0

the four vertices are coplanar and the three-dimensional cell loses its non-coplanar closure.

### Rigidity Condition

For a three-dimensional framework with N vertices, the six global rigid-body modes consist of three translations and three rotations.

After these six modes are removed, local rigidity requires the rigidity matrix R_G to reach:

rank R_G = 3N − 6

For a tetrahedron:

N = 4

therefore:

rank R_G = 6

The tetrahedron has exactly six edges, matching the number of independent constraints required for the minimal generic rigid framework in three dimensions.

### Reduced Stability Condition

The full stiffness matrix contains the six global rigid-body zero modes and therefore should not be tested by the condition:

det K_frame > 0

Instead, stability is evaluated in the reduced deformation subspace after removal of the rigid-body modes.

Let K_red denote the reduced stiffness matrix.

The local stability condition is:

λ_min(K_red) > 0

where λ_min(K_red) is the smallest eigenvalue associated with an internal deformation mode.

This condition means that every non-rigid infinitesimal deformation has a positive restoring stiffness.

### Phase Closure

The geometrical closure of the cell provides a minimal interaction loop through which relative phase relations can be retained and propagated.

For a closed cycle:

Σ_cycle Δφ_ij = 2πn

where n is an integer.

The tetrahedral cell extends this closure into a minimal non-coplanar three-dimensional structure containing multiple coupled triangular cycles.

### Consequence

The tetrahedron is therefore used in this framework as the minimal three-dimensional carrier satisfying:

- non-zero enclosed volume;
- non-coplanar geometric closure;
- six independent edge constraints;
- full generic rank after removal of rigid-body modes;
- positive reduced internal stiffness;
- multiple coupled phase-closure cycles.

More complex resonant structures can be represented as coupled assemblies of such cells, whose collective spectra and dynamical responses depend on topology, coupling strength, asymmetry, boundary conditions, and the inheritance of preceding dynamical states.

## Law 3. Node Oscillations → Frequencies (Quantization)

### Statement

A dynamically retained node supports characteristic oscillatory modes.

When the governing operator, geometry, and boundary conditions admit only discrete stationary solutions, the corresponding allowed frequencies form a discrete spectrum.

For an allowed mode:

E_n = h f_n

or equivalently:

E_n = ħω_n

with:

ω_n = 2πf_n

The discrete energy value is therefore associated with an allowed stationary mode of the system.

### Stationary Mode

Let:

Ψ_n(r,t) = ψ_n(r) e^(−iω_n t)

where:

- ψ_n(r) is the spatial mode;
- ω_n is its angular frequency.

For a time-independent Hermitian operator H:

Hψ_n = E_n ψ_n

with:

E_n = ħω_n

Therefore:

Hψ_n = ħω_n ψ_n

The allowed values {E_n} and {ω_n} are determined by the operator together with the governing boundary conditions.

### Discrete Spectrum

The spectral problem is:

Hψ_n = E_n ψ_n

subject to the required boundary conditions.

Only solutions compatible with those conditions belong to the admissible spectrum.

The resulting spectral sets are:

{E_n}

{ω_n}

{f_n}

with:

E_n = ħω_n = h f_n

Quantization therefore corresponds to discreteness of the admissible stationary spectrum rather than to arbitrary discretization of continuous motion.

### Phase Closure

For a closed stationary mode:

Δφ_n = 2πn

where n is an integer.

More generally, for a closed propagation path C:

∮_C dφ = 2πn

This condition expresses compatibility of the accumulated phase with closure of the mode.

The phase condition does not by itself determine the spectrum. The allowed mode must simultaneously satisfy:

- the governing dynamical equation;
- the geometry of the domain;
- the boundary conditions;
- the corresponding eigenvalue problem;
- the phase-closure condition.

### Mode Retention

An admissible eigenmode and a dynamically retained mode are related but not identical concepts.

The eigenvalue problem determines which stationary modes are mathematically allowed.

Dynamic retention determines whether a mode persists under:

- coupling;
- perturbation;
- dissipation;
- external drive;
- asymmetry;
- interaction with other modes.

The process is therefore:

**boundary conditions → admissible eigenmodes → characteristic frequencies → phase relations → dynamical retention or decay**

### Collective Extension

For multiple interacting phase-bearing modes, the individual frequencies alone do not determine the collective state.

The collective dynamics also depend on relative phase:

θ_j − θ_i

coupling:

W_ij

asymmetric phase lag:

γ

and external drive.

The transition from an isolated spectral mode to a collective dynamically retained state is therefore governed by both spectral admissibility and coupled phase evolution.

### Consequence

The spectral set:

{ω_n}

defines the characteristic allowed oscillatory modes of the system.

The dynamically realized state depends on which of those modes are excited, how they are coupled, whether their phase relations remain coherent, and whether the resulting state survives perturbation and dissipation.

In this framework, quantization and dynamical retention are therefore connected through the sequence:

**allowed mode → characteristic frequency → phase evolution → collective coherence or decoherence → persistence, transition, or decay**

## Law 4. Fractal Scaling

### Statement

Structural relations can recur across different scales when the governing dynamics preserve corresponding dimensionless ratios, phase relations, boundary conditions, or coupling topology.

Fractal scaling in this framework does not require different physical systems to be identical.

It describes the recurrence of dynamically related structural patterns under transformation of characteristic length and time scales.

### Scale Transformation

Let the spatial and temporal coordinates transform as:

r → b r

t → b^z t

where:

- `b` is the spatial scale factor;
- `z` is the dynamical scaling exponent.

A characteristic frequency transforms as:

f → f / b^z

and the corresponding angular frequency transforms as:

ω → ω / b^z

For a characteristic wavelength:

λ → b λ

The resulting scale relation is therefore:

f λ^z = const

when the same dynamical scaling exponent applies across the compared levels.

### Phase Relation Under Scaling

Let a phase field be represented by:

φ(r,t)

A scale-related phase structure satisfies:

φ(r,t) ↔ φ(b r, b^z t)

when the transformation preserves the relevant phase relations.

The requirement is not equality of absolute size or absolute frequency.

The relevant condition is preservation of the relation between:

- geometry;
- characteristic timescale;
- relative phase;
- coupling structure;
- boundary conditions.

### Ratio Invariants

For successive hierarchical levels:

f_(n+1) / f_n ≈ q_f

and:

λ_(n+1) / λ_n ≈ q_λ

where `q_f` and `q_λ` are approximately retained scaling ratios within the compared hierarchy.

Under the transformation:

λ_(n+1) = b λ_n

and:

f_(n+1) = f_n / b^z

the ratios satisfy:

q_λ ≈ b

q_f ≈ b^(−z)

Therefore:

q_f q_λ^z ≈ 1

This provides a direct relation between spatial scaling and characteristic frequency scaling.

### Collective Coherence Across Scales

For a scale level `l`, define the complex collective order parameter:

Z_l(t) = (1 / N_l) Σ_j exp(i θ_(l,j)(t))

with:

R_l(t) = |Z_l(t)|

The quantity `R_l(t)` measures collective phase coherence inside the corresponding scale level.

A relation between different levels does not require:

R_l(t) = R_(l+1)(t)

Instead, scale-related dynamics can be examined through the transformation of:

- characteristic frequencies;
- coherence profiles;
- coupling topology;
- transition boundaries;
- response to perturbation.

The general comparison is therefore:

{f_l, λ_l, R_l, W_l, boundary_l}

→ scaling transformation →

{f_(l+1), λ_(l+1), R_(l+1), W_(l+1), boundary_(l+1)}

### Recursive Structural Inheritance

A newly formed dynamical state does not begin from an abstract zero condition.

Its evolution begins from the state produced by the preceding dynamical process.

Let the state at level or cycle `n` be:

X_n

and let the next state be generated by a dynamical operator:

X_(n+1) = F_n(X_n, P_n)

where `P_n` represents the governing parameters and boundary conditions.

The next state therefore inherits the dynamically realized properties of the preceding state through its initial condition.

The process is:

**preceding state → transformed interaction conditions → phase evolution → new coherent or decoherent state → inherited next state**

This produces recursive inheritance of qualitative dynamical characteristics without requiring exact repetition of the preceding form.

### Asymmetry and Scale Development

Exact symmetry would reproduce an idealized identical transformation.

Observable structural development requires differences between successive dynamical states.

These differences can arise through:

- asymmetric coupling;
- phase lag;
- parameter drift;
- perturbation;
- dissipation;
- changing boundary conditions;
- branch selection.

The process is therefore:

**inheritance + asymmetry → differentiated trajectory → new structural state**

Fractal scaling in this framework is consequently not exact geometric copying.

It is the recurrence of related dynamical structure through scale transformation and inherited evolution.

### Consequence

Scale-related systems can be compared through preserved or transformed relations between:

- characteristic frequency;
- characteristic length;
- dynamical timescale;
- phase coherence;
- coupling topology;
- transition structure.

The proposed hierarchy:

atom → disk → galaxy

is therefore treated as a comparison of structural and dynamical relations across scales, not as an assertion that the underlying physical interactions are identical.

The general sequence is:

**local interaction → dynamically retained structure → inherited state → scale transformation → asymmetric evolution → new dynamically related structure**

## Law 5. Retention as Geometry

### Statement

In this framework, retention denotes the persistence and localization of a dynamically realized energy–momentum distribution.

In general relativity, such a distribution is not represented as an external force acting inside a fixed background. It contributes to the geometry of spacetime through the stress–energy tensor.

The mathematical sequence is:

**localized dynamical state → energy–momentum distribution → spacetime curvature → modified trajectories and causal structure**

The framework interprets this relation as the geometrical expression of dynamically retained energy.

### Newtonian Weak-Field Limit

For a point mass `M`, the Newtonian gravitational potential is:

Φ_N(r) = −GM / r

The potential energy of a test mass `m` is:

E_p = m Φ_N = −GMm / r

The gravitational field is:

g = −∇Φ_N

and the potential satisfies the Poisson equation:

∇²Φ_N = 4πGρ_m

where `ρ_m` is the mass density.

In the weak-field limit of general relativity, the metric component is approximately:

g_00 ≈ −(1 + 2Φ_N / c²)

The Newtonian potential therefore appears as the weak-field limit of spacetime geometry.

This provides the first mathematical bridge:

**localized mass–energy → gravitational potential → weak-field metric deformation**

### General-Relativistic Form

The Einstein field equations are:

G_μν + Λg_μν = (8πG / c⁴) T_μν

where:

- `G_μν` is the Einstein tensor;
- `g_μν` is the spacetime metric;
- `Λ` is the cosmological constant;
- `T_μν` is the stress–energy tensor.

The source of curvature is therefore not negative potential energy alone.

It is the full local stress–energy content represented by `T_μν`.

The corresponding variational formulation is based on the total action:

S = S_g + S_m

with gravitational part:

S_g = (c³ / 16πG) ∫ (R − 2Λ) √(−g) d⁴x

where:

- `R` is the Ricci scalar;
- `g` is the determinant of the metric tensor;
- `S_m` is the matter action.

Variation with respect to the metric gives:

δS / δg_μν = 0

which yields the Einstein field equations.

### Local Energy Density

For an observer with four-velocity `u^μ`, the locally measured energy density is:

ε = T_μν u^μ u^ν

The local dynamical distribution of energy and momentum is constrained by:

∇_μ T^μν = 0

This covariant conservation relation expresses the local continuity of energy–momentum evolution in curved spacetime.

Retention in this framework therefore refers to the persistence of a localized dynamical configuration whose energy–momentum distribution remains sufficiently structured over time.

### Phase Structure and Field Energy

For a complex field written as:

Ψ = A e^(iφ)

where:

- `A` is the amplitude;
- `φ` is the phase;

the spacetime derivative is:

∂_μΨ = e^(iφ) [∂_μA + iA ∂_μφ]

Therefore:

|∂_μΨ|²

contains contributions from both:

(∂_μA)²

and:

A²(∂_μφ)²

For field theories whose stress–energy tensor depends on derivatives of the field, spatial and temporal phase gradients can therefore contribute to the local energy–momentum distribution.

The mathematical bridge is:

**amplitude and phase structure → field derivatives → stress–energy distribution → spacetime geometry**

This does not mean that phase alone replaces the stress–energy tensor.

The phase structure enters through the dynamics of the underlying field.

### Dynamic Retention

A localized field configuration persists only if its internal dynamics remain compatible with its boundary conditions, interactions, dissipation, and perturbations.

The process is:

**localization → interaction → energy redistribution → coherence or decoherence → persistence, transition, or dispersal**

In the executable phase framework, the corresponding dynamical questions are examined through:

- collective phase coherence;
- perturbation response;
- transition candidates;
- path dependence;
- hysteresis;
- local Jacobians;
- spectral structure.

These computational quantities describe dynamical retention inside the implemented model.

The general-relativistic layer describes how a physical energy–momentum distribution is related to spacetime geometry.

### Consequence

The relation developed in this framework is not:

**negative potential energy = curvature**

but rather:

**dynamically retained physical state → localized energy–momentum distribution → geometrical response of spacetime**

In the weak-field limit, this relation reduces to the Newtonian gravitational potential.

In the full relativistic description, it is governed by the Einstein field equations.

The framework therefore uses the term retention as a dynamical bridge between the persistence of localized states and the geometrical response associated with their physical energy–momentum content.

## Law 6. Disk Instability and Accretion

### Statement

Rotating self-gravitating disks support coupled density, velocity, and gravitational perturbation modes.

When the restoring effects of pressure and rotation are insufficient to counter self-gravity, small perturbations can grow.

The resulting evolution is not determined by instability alone.

The nonlinear outcome depends on:

- the initial perturbation spectrum;
- local density;
- sound speed or velocity dispersion;
- differential rotation;
- dissipation;
- angular-momentum transport;
- coupling between growing modes;
- boundary conditions;
- preceding dynamical state.

The process is therefore:

**perturbation → mode growth or decay → nonlinear interaction → angular-momentum redistribution → branch selection → dynamically retained structure or dispersal**

### Local Dispersion Relation

For a local axisymmetric perturbation in a thin rotating disk, the standard dispersion relation is:

ω² = κ² − 2πGΣ|k| + c_s²k²

where:

- `ω` is the perturbation frequency;
- `κ` is the epicyclic frequency;
- `G` is the gravitational constant;
- `Σ` is the surface density;
- `k` is the radial wavenumber;
- `c_s` is the effective sound speed or velocity-dispersion scale.

The three terms represent competing dynamical contributions:

`κ²` — rotational stabilization

`−2πGΣ|k|` — self-gravitating amplification

`c_s²k²` — pressure or velocity-dispersion stabilization

When:

ω² > 0

the corresponding local linear mode is oscillatory.

When:

ω² < 0

the frequency becomes imaginary and the perturbation grows or decays exponentially.

Writing:

ω = iΓ

for an unstable mode gives:

Γ² = −ω²

where `Γ > 0` is the linear growth rate.

### Toomre Stability Parameter

The local axisymmetric stability parameter is:

Q = c_s κ / (πGΣ)

For the standard fluid-disk form:

Q > 1

corresponds to local stability against axisymmetric self-gravitating perturbations.

The threshold:

Q ≈ 1

marks the boundary between the locally stable and unstable regimes.

When:

Q < 1

a band of wavenumbers can satisfy:

ω² < 0

and the corresponding perturbations can grow.

The criterion identifies the onset of linear instability.

It does not by itself determine the final nonlinear structure.

### Characteristic Unstable Scale

The competition between self-gravity and pressure selects characteristic unstable wavelengths.

For the dispersion relation:

ω²(k) = κ² − 2πGΣ|k| + c_s²k²

the strongest local instability occurs near the wavenumber for which the gravitational and pressure contributions produce the minimum of `ω²(k)`.

For positive `k`:

dω² / dk = −2πGΣ + 2c_s²k

Setting:

dω² / dk = 0

gives the characteristic wavenumber:

k_* = πGΣ / c_s²

with corresponding wavelength:

λ_* = 2π / k_*

Therefore:

λ_* = 2c_s² / GΣ

This scale identifies a characteristic local wavelength of maximum linear susceptibility within the idealized thin-disk model.

### Mode Growth and Structural Development

A growing linear perturbation does not yet constitute a persistent structure.

As its amplitude increases, nonlinear interactions become important.

The evolution can include:

- mode coupling;
- wave steepening;
- shock formation;
- dissipation;
- fragmentation;
- angular-momentum exchange;
- redistribution of mass;
- formation of spirals, rings, clumps, or other collective structures.

The process is:

**linear instability → amplitude growth → nonlinear interaction → redistribution → dynamically selected structure**

The final state depends on the complete dynamical path.

### Phase Structure of Disk Modes

A perturbation mode can be represented as:

δX(r,φ,t) = A(r,t) exp[i(mφ + kr − ωt)]

where:

- `A(r,t)` is the mode amplitude;
- `m` is the azimuthal mode number;
- `k` is the radial wavenumber;
- `ω` is the mode frequency.

The phase is:

Φ(r,φ,t) = mφ + kr − ωt

Relative phase relations between interacting modes influence whether their contributions reinforce, cancel, transfer energy, or reorganize the resulting pattern.

For two modes:

ΔΦ = Φ_1 − Φ_2

A bounded relative phase can support persistent collective interaction.

A drifting relative phase can produce alternating reinforcement and cancellation.

The relevant dynamical question is therefore not merely whether a mode exists, but whether its amplitude and phase relations persist under interaction and dissipation.

### Collective Phase Coherence

For a set of interacting disk modes, define:

Z_disk(t) = [Σ_j a_j exp(iφ_j)] / Σ_j a_j

where:

- `a_j` is the amplitude of mode `j`;
- `φ_j` is its phase.

The collective phase coherence magnitude is:

R_disk(t) = |Z_disk(t)|

with:

0 ≤ R_disk(t) ≤ 1

This quantity can be used to describe the degree of collective phase alignment among the selected modes.

High `R_disk` does not by itself prove structural stability.

A dynamically retained pattern also depends on:

- mode amplitudes;
- growth and damping rates;
- angular-momentum transport;
- nonlinear coupling;
- dissipation;
- boundary conditions.

### Angular-Momentum Transport and Accretion

Accretion requires redistribution of angular momentum.

For a viscous thin-disk approximation, the mass accretion rate is commonly represented by:

Ṁ ≈ 3πνΣ

where:

- `Ṁ` is the accretion rate;
- `ν` is the effective kinematic viscosity;
- `Σ` is the surface density.

The effective transport can arise from several physical mechanisms, including hydrodynamic, gravitational, and magnetohydrodynamic stresses.

The general process is:

**stress or torque → angular-momentum redistribution → inward mass transport and outward angular-momentum transport**

In a mode-based description, coherent or partially coherent structures can participate in this redistribution through gravitational torques and correlated dynamical stresses.

### Asymmetry and Branch Selection

An exactly symmetric perturbation pattern would preserve an idealized balanced evolution.

Observable disk development depends on broken symmetry.

Sources of asymmetry include:

- unequal mode amplitudes;
- phase lag;
- differential rotation;
- spatial density gradients;
- external perturbations;
- nonlinear coupling;
- dissipation.

These asymmetries can produce different continuation paths even under similar current parameters.

The process is:

**instability → asymmetric mode interaction → different trajectories → nonlinear branch selection → path-dependent structure**

This creates a direct connection with the broader framework of transition boundaries and hysteresis.

### Dynamic Retention

A spiral, ring, clump, or other disk structure is dynamically retained only if the evolving interaction continues to support it.

The relevant question is not:

**Did an instability occur?**

but:

**Which structure survives the subsequent coupled evolution?**

The sequence is:

**instability → mode growth → nonlinear interaction → redistribution → coherence or decoherence → retention, transition, or dispersal**

### Consequence

Disk instability provides a mechanism for amplifying perturbations.

Accretion provides a mechanism for mass transport through angular-momentum redistribution.

Coupled phase evolution provides a way to describe the relative timing and collective interaction of the participating modes.

The framework therefore interprets rotating-disk structure through the combined relation:

**self-gravity + rotation + pressure or velocity dispersion + dissipation + asymmetric mode coupling + angular-momentum transport**

Persistent spirals, rings, filaments, or clumps are treated as dynamically selected states whose existence depends on the full nonlinear evolution rather than on the instability threshold alone.

## Law 7. Retention Limit (Black Hole)

### Statement

A black-hole horizon is treated in this framework as a limiting geometrical state of retention.

The physical condition is not defined by a critical phase density alone.

It arises when the distribution of mass–energy and the resulting spacetime geometry become sufficiently compact that outward-directed causal trajectories can no longer connect the interior region with distant external observers.

The process is:

**mass–energy concentration → increasing spacetime curvature → narrowing of outward causal escape directions → trapped region → horizon formation**

The phase-retention interpretation is applied only after this geometrical condition is defined.

### Compactness

For a gravitating system of mass `M` contained within a characteristic radius `R`, define the dimensionless compactness parameter:

C = 2GM / Rc²

where:

- `G` is the gravitational constant;
- `M` is the enclosed gravitating mass;
- `R` is the characteristic areal radius;
- `c` is the speed of light.

For a static, spherically symmetric Schwarzschild geometry, the horizon radius is:

r_s = 2GM / c²

and therefore:

C = 1

at:

R = r_s

The relation:

R > r_s

corresponds to a surface outside the Schwarzschild horizon.

The relation:

R = r_s

marks the horizon radius in the Schwarzschild solution.

The condition should not be generalized mechanically to arbitrary rotating, charged, or dynamical spacetimes without using the corresponding geometry.

### Schwarzschild Geometry

Outside a static, spherically symmetric gravitating mass, the metric is:

ds² = −(1 − 2GM / rc²)c²dt² + (1 − 2GM / rc²)^(−1)dr² + r²dΩ²

with:

dΩ² = dθ² + sin²θ dφ²

The horizon occurs at:

r = r_s = 2GM / c²

At this radius, the causal structure changes.

The horizon is not a material surface.

It is a null boundary separating trajectories that can still reach distant external observers from trajectories that cannot.

### Null Expansion and Trapped Surfaces

A more general dynamical description uses congruences of null rays orthogonal to a closed two-dimensional surface.

Let:

θ_+

denote the expansion of the outgoing null congruence, and:

θ_−

the expansion of the ingoing null congruence.

For an ordinary untrapped surface:

θ_+ > 0

and typically:

θ_− < 0

For a trapped surface:

θ_+ < 0

and:

θ_− < 0

Both future-directed null congruences then converge.

A marginally outer trapped surface satisfies:

θ_+ = 0

with:

θ_− < 0

This provides a local geometrical indicator associated with horizon formation in dynamical gravitational systems.

The transition is therefore described by:

**outgoing expansion positive → outgoing expansion decreases → marginal condition → trapped region**

### Retention as Causal Geometry

The defining property of the horizon is not that energy stops moving.

Local physical processes can remain dynamical.

The limiting condition concerns causal accessibility.

Inside the event horizon, future-directed causal trajectories remain directed toward the interior causal future and cannot return information to distant external observers.

The retention sequence is therefore:

**localized energy–momentum → curvature → causal deformation → trapped trajectories**

This is the geometrical meaning of the retention limit used in this framework.

### Energy–Momentum and Collapse

The formation of a trapped region requires a physical spacetime evolution.

The governing relation remains the Einstein field equation:

G_μν + Λg_μν = (8πG / c⁴) T_μν

The geometry therefore evolves in relation to the stress–energy tensor:

T_μν

A collapse process can involve:

- increasing compactness;
- pressure and stress evolution;
- radiation;
- angular momentum;
- asymmetry;
- changing causal structure.

The final geometry depends on the complete dynamical path.

Horizon formation is therefore not represented as an instantaneous algebra

Law 8. Emergent Stability (Macroscopic Phase-Lock)

Statement

Long-term stability of ensembles arises from large-N phase alignment.

Math

Kuramoto order parameter:

R(t) = (1/N) |Σ_(k=1)^N e^(iφ_k(t))|

R → 1 indicates coherence.

R → 0 indicates dephasing.

Consequence

Macro-stability requires large-scale high R.

Law of Energy Conservation — Resonant Form

Meaning

Energy is the measure of phase coherence; its conservation is the invariance of phase balance across modes and domains.

Local density and flux

d/dt ∫_V ρ_E dV = −∮_S J_E · dS

with:

ρ_E ∼ φ̇²

J_E ∼ φ̇ ∇φ

Spectral form

Σ_k E_k = Σ_k h f_k = const

Thermodynamics in phase variables

dU = δQ − δW

corresponds to:

∮ dφ = 2πn

Entropy:

S ∝ −Σ_k p_k ln p_k

Entropy growth:

dS/dt ≥ 0

corresponds to dephasing growth.

Equilibrium

A phase-stationary state:

∂_t φ ≈ const

minimizes dissipation.

The “cold limit” is perfect PL, not absence of motion.

Mathematical Minimum

E = h f

ħ = h / 2π

Schrödinger equation:

(ħ² / 2m) ∇²ψ + Uψ = iħ ∂ψ / ∂t

Jeans length:

λ_J = √(πc_s² / Gρ)

Toomre criterion:

Q = c_s κ / (πGΣ)

Hill radius:

r_H = a(m / 3M)^(1/3)

Accretion rate:

Ṁ ≈ 3πνΣ

Schwarzschild radius:

r_s = 2GM / c²

Black-hole entropy:

S = k_B c³ A / (4Għ)

Hawking temperature:

T_H = ħc³ / (8πGMk_B)

ISCO frequency approximation:

f_ISCO ≈ 2200 Hz × M_☉ / M

Unifying Chain — Micro → Macro

δ-source → minimal form → node oscillations (hf) → fractal folding → retention = curvature → instabilities + accretion → horizons → macroscopic PL

Quantum Mechanics via Resonance

Full Schrödinger Framework in Phase Language

Time-dependent Schrödinger equation:

iħ ∂ψ(r,t) / ∂t = [−(ħ² / 2m)∇² + U(r,t)] ψ(r,t)

Stationary states:

ψ(r,t) = ψ_n(r) e^(−iω_n t)

ħω_n = E_n

Hψ_n = E_n ψ_n

Nodes and boundary conditions

Stable nodes satisfy phase closure:

Δφ = 2πn

under boundary conditions and action extremum.

Probability Current and Continuity

Probability density:

ρ = |ψ|²

Probability current:

j = (ħ / m) Im(ψ∗∇ψ)

Continuity relation:

∂ρ / ∂t + ∇ · j = 0

Madelung representation:

ψ = √ρ e^(iφ)

which gives:

∂ρ / ∂t + ∇ · [ρ(ħ / m)∇φ] = 0

and:

∂φ / ∂t + (ħ / 2m)|∇φ|² + (U + Q) / ħ = 0

with:

Q = −(ħ² / 2m) (∇²√ρ / √ρ)

Observer, Collapse, and Phase-Lock

Measurement = local phase-lock:

|φ_obs − φ_sys| ≤ Δφ_lock

Decoherence = dephasing from the environment.

Tunneling as Phase Resonance

WKB approximation

For:

U(x) > E

the transmission coefficient is:

T_WKB ≈ exp[−2 ∫_(x₁)^(x₂) κ(x) dx]

where:

κ(x) = √(2m[U(x) − E]) / ħ

Rectangular Barrier

For barrier width a and height V:

k = √(2mE) / ħ

κ = √(2m(V − E)) / ħ

For E < V:

T = 1 / [1 + V² sinh²(κa) / 4E(V − E)]

For E > V:

T = 1 / [1 + V² sin²(qa) / 4E(E − V)]

where:

q = √(2m(E − V)) / ħ

Resonant peaks correspond to boundary phase alignment — Fabry–Pérot-like PL.

Time–Energy in Phase Variables

Short Δt limits phase resolution:

Δφ ∼ ωΔt

The relation:

ΔE Δt ≳ ħ / 2

represents a minimal phase area in the (E,t) domain.

Neutron-Star Collisions: Phase Retuning of Nodes

Standard r-process nucleosynthesis is recast as deep phase retuning of nuclear-matter nodes under extreme boundary conditions.

Stable nuclei are new nodes of the field; abundance tracks PL pathways.

Frequency invariant:

f_ISCO ≈ 2200 Hz × M_☉ / M

This links spectral peaks to mass.

Saturn’s Hexagon: Standing-Wave Resonator

Mechanism

Angular quantization in a polar jet loop:

kR ≈ 6

Stability

A Floquet multiplier below 1 maintains the limit cycle; the boundary acts as a waveguide preserving PL around the ring.

The Great Attractor: A Synchronization Node of Scale

View

Not an unknown pull, but a PL node of the large-scale velocity field; flows align toward the phase-stable region.

Condition

Near-irrotational field:

∇ × v ≈ 0

with quasi-static phase yields coherent mass flux:

j ∝ ρv

Engineering Note: Toward “Cold” Plasma via Phase Synchronization

Two- or three-tone drive:

f₁, f₂, f_c

Phase feedback using PLL with capacitive or optical probe; target phase:

φ₀

Entry criterion:

disappearance of phase slips and a narrow noise band.

Magnetic trap:

passive protector, not main retainer.

Goal

A stable low-temperature plasma mode held by PL, not heat.

The Boötes Void (“Black Nothing”): Resonant Interpretation

Thesis

The Boötes Void is a large-scale dephasing zone, not an absence of matter: long-wave density modes cancel amplitudes, preventing node formation; filaments reside on the PL perimeter.

Mechanism — Resonance

On scale L, a set of long modes {Φ_L,i} sums to a net phase satisfying:

|ΔΦ_L| ≳ π

which implies:

node suppression — growth inhibited.

On the boundary, local PL holds; filaments and clusters accumulate where closure occurs.

Physical Reading

Not vacuum; a stable resonant state with low node density and long coherence time.

“Blackness” is the lack of bright internal sources, not absence of field or energy.

Predictions and Tests

1. Velocity fields

Radial outflow toward walls through peculiar velocities, with minimal shear inside.

2. Weak lensing

Suppressed inside, enhanced on the rim due to filaments.

3. ISW signature

Anomalous CMB imprint across the supervoid through a modified Sachs–Wolfe effect.

4. Ages and metallicity

Deficit of young populations inside, enhanced activity on the rim.

5. Fluctuation spectrum

Higher power at ring-like or polygonal harmonics corresponding to the perimeter; central modes suppressed.

One-Liner

The Boötes Void is a stable anti-node of the Universe’s resonant lattice: a dephased core with a phase-locked, structure-rich boundary.

Experimental Checklist

Tunneling

Boundary phase shifts; transparency changes with parametric phase tuning.

Plasma

Stable-phase low-temperature mode; narrow-band noise.

Asteroseismology

Frequency peaks ↔ mean density ↔ mass through f_ISCO.

Saturn’s Hexagon

Angular quantization of persistent flow harmonics.

Great Attractor

Phase-coherent velocity-field maps.

Boötes Void

Weak lensing, velocity fields, and ISW imprint.

Human as a Resonant Contour

Model

The organism is an ensemble of coupled oscillators — neural, cardiorespiratory, and endocrine — phase-locked across bands; perception is multi-PLL reconstruction of external fields.

Neural Bands — Illustrative

Delta: 0.5–4 Hz

Theta: 4–8 Hz

Alpha: 8–13 Hz

Beta: 13–30 Hz

Gamma: 30–100+ Hz

Define a coherence matrix:

C_ij(f)

and a global order parameter:

R_f = (1/N) |Σ_j e^(iφ_j(f))|

Cognitive states map to profiles of {R_f}.

Multisensory PL

Vision: retina → thalamocortical PL.

Audition: cochlear tonotopy as narrowband PLLs.

Somatosensation: phase-coded transients.

Proprioception closes the body loop.

Madelung-Style Neural Field

ψ = √ρ e^(iφ)

which gives flow:

v = (ħ / m∗)∇φ

with effective mass m∗ as a phenomenological parameter.

Stable percepts are phase-retained nodes.

Emotion and Control

Slow modulators — vagal tone and neuromodulators — tune coupling K and noise σ, shifting PL basins.

Plasticity implements memory through Hebbian adaptation:

ΔW ∝ x_i x_j

Creativity / “Eureka”

Rapid global PL on near-resonant manifolds.

Note

Theoretical, non-medical; proposes measurable correlates:

R_f

C_ij(f)

License and Citation

CC BY 4.0

Marnov, Maksym (Alchimist). (2025). Physics of Resonance: From the Singularity Point to the Event Horizon. POSITRON–ISKORKA Project.
