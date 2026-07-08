#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# RPU · Minimal Resonant Core (v0.5, balanced ternary control)
# License: Apache-2.0 (see /LICENSE_CODE)

import argparse

import numpy as np


TAU = 2.0 * np.pi


def power_iteration_radius(A, iters=128, rng=None):
    matrix = np.asarray(A, dtype=float)

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("A must be a square matrix")

    if matrix.shape[0] == 0:
        raise ValueError("A must not be empty")

    if int(iters) <= 0:
        raise ValueError("iters must be positive")

    generator = np.random.default_rng(None if rng is None else rng)
    x = generator.normal(size=matrix.shape[0])
    norm = np.linalg.norm(x)

    if norm == 0.0:
        x = np.ones(matrix.shape[0], dtype=float)
        norm = np.linalg.norm(x)

    x = x / norm
    radius = 0.0

    for _ in range(int(iters)):
        x = matrix @ x
        norm = np.linalg.norm(x)

        if norm <= 1.0e-12:
            return 0.0

        x = x / norm
        radius = norm

    return float(radius)


def quantize_balanced(x, t0=0.0, t1=0.33):
    del t0

    values = np.asarray(x, dtype=float)
    threshold = float(t1)

    if not np.isfinite(threshold) or threshold < 0.0:
        raise ValueError("t1 must be a finite non-negative value")

    q = np.zeros_like(values, dtype=np.int8)
    q[values >= threshold] = 1
    q[values <= -threshold] = -1
    return q


def quantize_W(W, thresh=0.2):
    weights = np.asarray(W, dtype=float)
    threshold = float(thresh)

    if not np.isfinite(threshold) or threshold < 0.0:
        raise ValueError("thresh must be a finite non-negative value")

    states = np.zeros_like(weights, dtype=np.int8)
    states[weights >= threshold] = 1
    states[weights <= -threshold] = -1
    return states


class RPUCore:
    def __init__(
        self,
        N,
        seed=42,
        k_global=0.6,
        dt=5e-3,
        sigma=0.02,
        sparsify=0.0,
        threshold=None,
        norm_iters=128,
        gamma=np.pi * 0.3,
        anti_R=0.90,
        anti_duration=200,
        anti_amp_scale=0.7,
        anti_sigma_boost=0.01,
        mod_amp_freq=0.1,
        mod_amp_depth=0.1,
        mod_freq_depth=0.02,
        ternary=True,
        wq_thresh=0.25,
        state_tau=0.33,
    ):
        self.N = int(N)
        if self.N <= 0:
            raise ValueError("N must be positive")

        self.dt = float(dt)
        if not np.isfinite(self.dt) or self.dt <= 0.0:
            raise ValueError("dt must be a finite positive value")

        self.kg = float(k_global)
        self.sigma_base = float(sigma)
        self.gamma = float(gamma)
        self.wq_thresh = float(wq_thresh)
        self.state_tau = float(state_tau)

        if not np.isfinite(self.kg):
            raise ValueError("k_global must be finite")

        if not np.isfinite(self.sigma_base) or self.sigma_base < 0.0:
            raise ValueError("sigma must be a finite non-negative value")

        if not np.isfinite(self.gamma):
            raise ValueError("gamma must be finite")

        if not np.isfinite(self.wq_thresh) or self.wq_thresh < 0.0:
            raise ValueError(
                "wq_thresh must be a finite non-negative value"
            )

        if not np.isfinite(self.state_tau) or self.state_tau < 0.0:
            raise ValueError(
                "state_tau must be a finite non-negative value"
            )

        self.rng = np.random.default_rng(seed)

        self.omega = self.rng.normal(
            TAU * 1.0,
            TAU * 0.10,
            self.N,
        )

        self.theta = self.rng.uniform(
            0.0,
            TAU,
            self.N,
        )

        W = self.rng.normal(
            0.0,
            1.0,
            (self.N, self.N),
        )

        W = (W + W.T) / 2.0
        np.fill_diagonal(W, 0.0)

        max_abs = float(np.max(np.abs(W)))

        if max_abs > 0.0:
            W = W / max_abs

        if threshold is not None:
            threshold_value = float(threshold)

            if (
                not np.isfinite(threshold_value)
                or threshold_value < 0.0
            ):
                raise ValueError(
                    "threshold must be a finite non-negative value"
                )

            W = W * (
                np.abs(W) >= threshold_value
            )

        elif float(sparsify) > 0.0:
            sparsify_value = float(sparsify)

            if (
                not np.isfinite(sparsify_value)
                or not 0.0 <= sparsify_value <= 1.0
            ):
                raise ValueError(
                    "sparsify must be within [0, 1]"
                )

            cutoff = np.quantile(
                np.abs(W),
                sparsify_value,
            )

            W = W * (
                np.abs(W) >= cutoff
            )

        rho = power_iteration_radius(
            W,
            iters=norm_iters,
            rng=seed,
        )

        if rho > 1.0:
            W = W / rho

        self.W = W

        self.ext_freq = np.zeros(
            self.N,
            dtype=float,
        )

        self.ext_amp = np.zeros(
            self.N,
            dtype=float,
        )

        self.ext_phase = np.zeros(
            self.N,
            dtype=float,
        )

        self.mod_amp_freq = float(
            mod_amp_freq
        )

        self.mod_amp_depth = float(
            mod_amp_depth
        )

        self.mod_freq_depth = float(
            mod_freq_depth
        )

        if not np.isfinite(self.mod_amp_freq):
            raise ValueError(
                "mod_amp_freq must be finite"
            )

        if not np.isfinite(self.mod_amp_depth):
            raise ValueError(
                "mod_amp_depth must be finite"
            )

        if not np.isfinite(self.mod_freq_depth):
            raise ValueError(
                "mod_freq_depth must be finite"
            )

        self.anti_R = float(anti_R)
        self.anti_duration = int(
            anti_duration
        )

        self.anti_amp_scale = float(
            anti_amp_scale
        )

        self.anti_sigma_boost = float(
            anti_sigma_boost
        )

        if not np.isfinite(self.anti_R):
            raise ValueError(
                "anti_R must be finite"
            )

        if self.anti_duration < 0:
            raise ValueError(
                "anti_duration must be non-negative"
            )

        if not np.isfinite(
            self.anti_amp_scale
        ):
            raise ValueError(
                "anti_amp_scale must be finite"
            )

        if (
            not np.isfinite(
                self.anti_sigma_boost
            )
            or self.anti_sigma_boost < 0.0
        ):
            raise ValueError(
                "anti_sigma_boost must be "
                "a finite non-negative value"
            )

        self._antilock_timer = 0
        self._amp_scale_dyn = 1.0

        self.use_ternary = bool(
            ternary
        )

        self.Wq = quantize_W(
            self.W,
            thresh=self.wq_thresh,
        )

        self.s = quantize_balanced(
            np.cos(self.theta),
            t1=self.state_tau,
        )

        self.t = 0.0

    def _validate_profile(
        self,
        values,
        name,
    ):
        profile = np.asarray(
            values,
            dtype=float,
        )

        if profile.size != self.N:
            raise ValueError(
                f"{name} size mismatch: "
                f"expected {self.N}, "
                f"got {profile.size}"
            )

        profile = profile.reshape(
            self.N
        )

        if not np.all(
            np.isfinite(profile)
        ):
            raise ValueError(
                f"{name} must contain "
                "only finite values"
            )

        return profile.copy()

    def mix(
        self,
        a,
        b,
        alpha=0.5,
    ):
        first = np.asarray(
            a,
            dtype=float,
        )

        second = np.asarray(
            b,
            dtype=float,
        )

        alpha_value = float(
            alpha
        )

        if first.shape != second.shape:
            raise ValueError(
                "a and b must have "
                "the same shape"
            )

        if (
            not np.all(np.isfinite(first))
            or not np.all(
                np.isfinite(second)
            )
        ):
            raise ValueError(
                "a and b must contain "
                "only finite values"
            )

        if not np.isfinite(alpha_value):
            raise ValueError(
                "alpha must be finite"
            )

        return (
            (1.0 - alpha_value) * first
            + alpha_value * second
        )

    def lock(
        self,
        freq_profile=None,
        amp_profile=None,
        reset_phase=False,
    ):
        if freq_profile is not None:
            self.ext_freq = (
                self._validate_profile(
                    freq_profile,
                    "freq_profile",
                )
            )

        if amp_profile is not None:
            self.ext_amp = (
                self._validate_profile(
                    amp_profile,
                    "amp_profile",
                )
            )

        if reset_phase:
            self.ext_phase = np.zeros(
                self.N,
                dtype=float,
            )

    def reset_phases(
        self,
        theta=None,
    ):
        if theta is None:
            self.theta = (
                self.rng.uniform(
                    0.0,
                    TAU,
                    self.N,
                )
            )

        else:
            self.theta = (
                self._validate_profile(
                    theta,
                    "theta",
                )
                % TAU
            )

        self.s = quantize_balanced(
            np.cos(self.theta),
            t1=self.state_tau,
        )

    def _order_param(
        self,
        theta=None,
    ):
        phases = (
            self.theta
            if theta is None
            else np.asarray(
                theta,
                dtype=float,
            )
        )

        if phases.size != self.N:
            raise ValueError(
                "theta size mismatch: "
                f"expected {self.N}, "
                f"got {phases.size}"
            )

        phases = phases.reshape(
            self.N
        )

        z = np.exp(
            1j * phases
        )

        mean_z = np.mean(z)

        return (
            float(np.abs(mean_z)),
            float(np.angle(mean_z)),
        )

    def measure(
        self,
        kind="order",
    ):
        if kind == "order":
            R, phi = (
                self._order_param()
            )

            return {
                "R": R,
                "phi": phi,
            }

        if kind == "clusters":
            labels = np.sign(
                np.cos(self.theta)
            ).astype(int)

            return {
                "labels": labels.tolist()
            }

        if kind == "phases":
            return {
                "theta": self.theta.copy()
            }

        if kind == "ternary":
            return {
                "s": self.s.copy(),
                "Wq_nnz": int(
                    np.count_nonzero(
                        self.Wq
                    )
                ),
            }

        raise ValueError(
            "unknown metric"
        )

    def imprint(
        self,
        pattern,
        gain=0.25,
    ):
        values = (
            self._validate_profile(
                pattern,
                "pattern",
            )
        )

        gain_value = float(
            gain
        )

        if not np.isfinite(gain_value):
            raise ValueError(
                "gain must be finite"
            )

        std = float(
            values.std()
        )

        if std <= 1.0e-12:
            raise ValueError(
                "pattern must have "
                "non-zero variance"
            )

        normalized = (
            values - values.mean()
        ) / std

        hebbian = np.outer(
            normalized,
            normalized,
        )

        np.fill_diagonal(
            hebbian,
            0.0,
        )

        max_abs = float(
            np.max(
                np.abs(hebbian)
            )
        )

        if max_abs > 0.0:
            hebbian = (
                hebbian / max_abs
            )

        self.W = np.tanh(
            self.W
            + gain_value * hebbian
        )

        self.Wq = quantize_W(
            self.W,
            thresh=self.wq_thresh,
        )

    def _dtheta(
        self,
        theta,
        ext_phase,
        amp_now,
    ):
        phase_diff = (
            theta[:, None]
            - theta[None, :]
        )

        coupling = np.sum(
            self.W
            * np.sin(
                -phase_diff
                - self.gamma
            ),
            axis=1,
        )

        pll = (
            amp_now
            * np.sin(
                ext_phase - theta
            )
        )

        return (
            self.omega
            + self.kg * coupling
            + pll
        )

    def _ternary_controller(
        self,
    ):
        raw_control = (
            self.Wq @ self.s
        )

        degree = np.maximum(
            np.sum(
                np.abs(self.Wq),
                axis=1,
            ),
            1,
        )

        normalized_control = (
            raw_control / degree
        )

        ternary_control = (
            quantize_balanced(
                normalized_control,
                t1=0.2,
            )
            .astype(float)
        )

        return (
            0.15 * ternary_control
        )

    def step(
        self,
        steps=1,
        stability_guard=True,
    ):
        step_count = int(
            steps
        )

        if step_count < 0:
            raise ValueError(
                "steps must be non-negative"
            )

        for _ in range(
            step_count
        ):
            if (
                self._antilock_timer
                > 0
            ):
                amp_scale = (
                    self.anti_amp_scale
                )

                sigma = (
                    self.sigma_base
                    + self.anti_sigma_boost
                )

                self._antilock_timer -= 1

            else:
                amp_scale = 1.0
                sigma = self.sigma_base

            self._amp_scale_dyn = (
                amp_scale
            )

            amp_modulation = (
                1.0
                + self.mod_amp_depth
                * np.sin(
                    TAU
                    * self.mod_amp_freq
                    * self.t
                )
            )

            amp_now = (
                self.ext_amp
                * amp_scale
                * amp_modulation
            )

            freq_modulation = (
                1.0
                + self.mod_freq_depth
                * np.sin(
                    TAU
                    * self.mod_amp_freq
                    * 0.5
                    * self.t
                )
            )

            freq_now = (
                self.ext_freq
                * freq_modulation
            )

            if self.use_ternary:
                phase_bump = (
                    self._ternary_controller()
                )

            else:
                phase_bump = (
                    np.zeros(
                        self.N,
                        dtype=float,
                    )
                )

            if stability_guard:
                scale = (
                    self.kg
                    + float(
                        np.max(
                            np.abs(
                                amp_now
                            )
                        )
                    )
                )

                factor = (
                    scale * self.dt
                )

                if factor > 0.1:
                    self.dt = (
                        0.1
                        / max(
                            scale,
                            1.0e-12,
                        )
                    )

            self.ext_phase = (
                self.ext_phase
                + self.dt * freq_now
                + phase_bump
            ) % TAU

            k1 = self._dtheta(
                self.theta,
                self.ext_phase,
                amp_now,
            )

            predictor = (
                self.theta
                + self.dt * k1
            ) % TAU

            k2 = self._dtheta(
                predictor,
                self.ext_phase,
                amp_now,
            )

            dtheta = (
                0.5 * (k1 + k2)
            )

            dtheta += (
                sigma
                * self.rng.normal(
                    0.0,
                    1.0,
                    self.N,
                )
            )

            self.theta = (
                self.theta
                + self.dt * dtheta
            ) % TAU

            self.t += self.dt

            if self.use_ternary:
                self.s = (
                    quantize_balanced(
                        np.cos(
                            self.theta
                        ),
                        t1=self.state_tau,
                    )
                )

            R, _ = (
                self._order_param()
            )

            if (
                R > self.anti_R
                and self._antilock_timer
                == 0
            ):
                self._antilock_timer = (
                    self.anti_duration
                )


def build_core(args):
    return RPUCore(
        args.N,
        seed=args.seed,
        k_global=args.k,
        dt=args.dt,
        sigma=args.sigma,
        sparsify=args.sparsify,
        threshold=args.threshold,
        norm_iters=args.norm_iters,
        gamma=args.gamma,
        anti_R=args.anti_R,
        anti_duration=args.anti_duration,
        anti_amp_scale=(
            args.anti_amp_scale
        ),
        anti_sigma_boost=(
            args.anti_sigma_boost
        ),
        mod_amp_freq=(
            args.mod_amp_freq
        ),
        mod_amp_depth=(
            args.mod_amp_depth
        ),
        mod_freq_depth=(
            args.mod_freq_depth
        ),
        ternary=(
            not args.no_ternary
        ),
        wq_thresh=args.wq_thresh,
        state_tau=args.state_tau,
    )


def prepare_profiles(N):
    x = np.linspace(
        0.0,
        TAU,
        N,
        endpoint=False,
    )

    profile_A = (
        1.0
        + 0.2
        * np.sin(
            3.0 * x
        )
    )

    profile_B = (
        1.0
        + 0.2
        * np.sin(
            7.0 * x
            + np.pi / 4.0
        )
    )

    imprint_A = np.sin(
        3.0 * x
    )

    imprint_B = np.sin(
        7.0 * x
        + np.pi / 4.0
    )

    return (
        x,
        profile_A,
        profile_B,
        imprint_A,
        imprint_B,
    )


def run_once(args):
    rpu = build_core(args)

    (
        _,
        profile_A,
        profile_B,
        imprint_A,
        imprint_B,
    ) = prepare_profiles(
        args.N
    )

    rpu.imprint(
        imprint_A,
        gain=0.25,
    )

    rpu.imprint(
        imprint_B,
        gain=0.25,
    )

    mix_ab = rpu.mix(
        profile_A,
        profile_B,
        alpha=args.alpha,
    )

    rpu.lock(
        freq_profile=(
            TAU * mix_ab
        ),
        amp_profile=(
            args.amp
            * np.ones(args.N)
        ),
        reset_phase=True,
    )

    log_R = []
    log_phi = []

    for tact in range(
        1,
        args.steps + 1,
    ):
        rpu.step(
            1,
            stability_guard=(
                not args.no_guard
            ),
        )

        if (
            tact
            % args.log_every
            == 0
            or tact == args.steps
        ):
            measurement = (
                rpu.measure("order")
            )

            log_R.append(
                measurement["R"]
            )

            log_phi.append(
                measurement["phi"]
            )

    order = rpu.measure(
        "order"
    )

    clusters = rpu.measure(
        "clusters"
    )

    ternary = rpu.measure(
        "ternary"
    )

    unique_clusters = (
        np.unique(
            clusters["labels"]
        )
        .tolist()
    )

    print(
        f"[run] R={order['R']:.3f}, "
        f"meanφ={order['phi']:.3f} rad; "
        f"clusters={unique_clusters} "
        f"(sample "
        f"{clusters['labels'][:24]})"
    )

    print(
        f"[ternary] "
        f"nnz(Wq)="
        f"{ternary['Wq_nnz']}, "
        f"s-sample="
        f"{ternary['s'][:24].tolist()}"
    )

    print(
        f"[diag] R(t) "
        f"samples={len(log_R)} → "
        f"{np.array2string("
        f"np.array(log_R), "
        f"precision=3, "
        f"separator=', '"
        f")}"
    )

    print(
        f"[diag] φ(t) "
        f"samples={len(log_phi)} → "
        f"{np.array2string("
        f"np.array(log_phi), "
        f"precision=3, "
        f"separator=', '"
        f")}"
    )


def run_scan(args):
    rpu = build_core(args)

    (
        _,
        profile_A,
        profile_B,
        imprint_A,
        imprint_B,
    ) = prepare_profiles(
        args.N
    )

    rpu.imprint(
        imprint_A,
        gain=0.25,
    )

    rpu.imprint(
        imprint_B,
        gain=0.25,
    )

    alphas = np.linspace(
        0.0,
        1.0,
        args.scan_points,
    )

    R_values = []
    cluster_counts = []

    for alpha in alphas:
        mix_ab = rpu.mix(
            profile_A,
            profile_B,
            alpha=alpha,
        )

        rpu.lock(
            freq_profile=(
                TAU * mix_ab
            ),
            amp_profile=(
                args.amp
                * np.ones(args.N)
            ),
            reset_phase=True,
        )

        rpu.reset_phases()

        for _ in range(
            args.scan_steps
        ):
            rpu.step(
                1,
                stability_guard=(
                    not args.no_guard
                ),
            )

        order = rpu.measure(
            "order"
        )

        clusters = rpu.measure(
            "clusters"
        )

        cluster_count = len(
            set(
                clusters["labels"]
            )
        )

        R_values.append(
            order["R"]
        )

        cluster_counts.append(
            cluster_count
        )

        print(
            f"[scan] α={alpha:.3f} → "
            f"R={order['R']:.3f}, "
            f"clusters={cluster_count}"
        )

    R_values = np.asarray(
        R_values
    )

    cluster_counts = np.asarray(
        cluster_counts
    )

    R_jumps = np.where(
        np.abs(
            np.diff(R_values)
        )
        > args.jump_thresh
    )[0]

    cluster_switches = np.where(
        np.diff(
            cluster_counts
        )
        != 0
    )[0]

    candidate_indices = sorted(
        set(
            R_jumps.tolist()
            + cluster_switches.tolist()
        )
    )

    candidates = [
        round(
            float(
                alphas[index]
            ),
            3,
        )
        for index
        in candidate_indices
    ]

    print(
        "[scan] candidate "
        "bifurcations at "
        f"α≈ {candidates}"
    )

    print(
        f"[scan] R(α) = "
        f"{np.array2string("
        f"R_values, "
        f"precision=3, "
        f"separator=', '"
        f")}"
    )

    print(
        f"[scan] K(α) = "
        f"{cluster_counts.tolist()}"
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "RPU · Minimal Resonant Core "
            "v0.5 (balanced ternary)"
        )
    )

    parser.add_argument(
        "--N",
        type=int,
        default=256,
    )

    parser.add_argument(
        "--k",
        type=float,
        default=0.6,
    )

    parser.add_argument(
        "--dt",
        type=float,
        default=5e-3,
    )

    parser.add_argument(
        "--steps",
        type=int,
        default=3000,
    )

    parser.add_argument(
        "--alpha",
        type=float,
        default=0.35,
    )

    parser.add_argument(
        "--amp",
        type=float,
        default=0.28,
    )

    parser.add_argument(
        "--sigma",
        type=float,
        default=0.03,
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=42,
    )

    parser.add_argument(
        "--log-every",
        type=int,
        default=50,
    )

    parser.add_argument(
        "--sparsify",
        type=float,
        default=0.8,
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=None,
    )

    parser.add_argument(
        "--norm-iters",
        type=int,
        default=96,
    )

    parser.add_argument(
        "--no-guard",
        action="store_true",
    )

    parser.add_argument(
        "--gamma",
        type=float,
        default=np.pi * 0.3,
    )

    parser.add_argument(
        "--anti-R",
        type=float,
        default=0.90,
    )

    parser.add_argument(
        "--anti-duration",
        type=int,
        default=200,
    )

    parser.add_argument(
        "--anti-amp-scale",
        type=float,
        default=0.7,
    )

    parser.add_argument(
        "--anti-sigma-boost",
        type=float,
        default=0.01,
    )

    parser.add_argument(
        "--mod-amp-freq",
        type=float,
        default=0.1,
    )

    parser.add_argument(
        "--mod-amp-depth",
        type=float,
        default=0.1,
    )

    parser.add_argument(
        "--mod-freq-depth",
        type=float,
        default=0.02,
    )

    parser.add_argument(
        "--no-ternary",
        action="store_true",
    )

    parser.add_argument(
        "--wq-thresh",
        type=float,
        default=0.25,
    )

    parser.add_argument(
        "--state-tau",
        type=float,
        default=0.33,
    )

    parser.add_argument(
        "--scan",
        action="store_true",
    )

    parser.add_argument(
        "--scan-points",
        type=int,
        default=21,
    )

    parser.add_argument(
        "--scan-steps",
        type=int,
        default=1000,
    )

    parser.add_argument(
        "--jump-thresh",
        type=float,
        default=0.05,
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.scan:
        run_scan(args)
    else:
        run_once(args)
