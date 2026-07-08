#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate validated dissipative Bloch trajectories for the quasi-TWA demo."""

from __future__ import annotations

import argparse
import csv
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

import numpy as np


DEFAULT_GAMMA_RATIOS = (
    0.1,
    0.2,
    0.5,
    1.0,
)

DEFAULT_LOGS_DIR = (
    Path(__file__).resolve().parent
    / "logs"
)


@dataclass(frozen=True)
class Params:
    """Numerical parameters for one driven dissipative Bloch trajectory."""

    Omega: float
    gamma: float
    delta: float
    T: float
    dt: float
    s0: np.ndarray

    def validated(self) -> "Params":
        Omega = float(
            self.Omega
        )

        gamma = float(
            self.gamma
        )

        delta = float(
            self.delta
        )

        T = float(
            self.T
        )

        dt = float(
            self.dt
        )

        s0 = np.asarray(
            self.s0,
            dtype=float,
        )

        if (
            not np.isfinite(
                Omega
            )
            or Omega <= 0.0
        ):
            raise ValueError(
                "Omega must be a finite "
                "positive value"
            )

        if (
            not np.isfinite(
                gamma
            )
            or gamma <= 0.0
        ):
            raise ValueError(
                "gamma must be a finite "
                "positive value"
            )

        if not np.isfinite(
            delta
        ):
            raise ValueError(
                "delta must be finite"
            )

        if (
            not np.isfinite(
                T
            )
            or T <= 0.0
        ):
            raise ValueError(
                "T must be a finite "
                "positive value"
            )

        if (
            not np.isfinite(
                dt
            )
            or dt <= 0.0
        ):
            raise ValueError(
                "dt must be a finite "
                "positive value"
            )

        if dt > T:
            raise ValueError(
                "dt must not exceed T"
            )

        if s0.shape != (
            3,
        ):
            raise ValueError(
                "s0 must contain exactly "
                "three components: "
                "[sx, sy, sz]"
            )

        if not np.all(
            np.isfinite(
                s0
            )
        ):
            raise ValueError(
                "s0 must contain only "
                "finite values"
            )

        return Params(
            Omega=Omega,
            gamma=gamma,
            delta=delta,
            T=T,
            dt=dt,
            s0=s0.copy(),
        )


def rk4_step(
    function: Callable[..., np.ndarray],
    y: np.ndarray,
    t: float,
    h: float,
    args: Sequence[float],
) -> np.ndarray:
    """Advance one fixed RK4 step."""

    state = np.asarray(
        y,
        dtype=float,
    )

    step = float(
        h
    )

    if state.shape != (
        3,
    ):
        raise ValueError(
            "RK4 state must have "
            "shape (3,)"
        )

    if not np.all(
        np.isfinite(
            state
        )
    ):
        raise ValueError(
            "RK4 state must contain "
            "only finite values"
        )

    if not np.isfinite(
        t
    ):
        raise ValueError(
            "RK4 time must be finite"
        )

    if (
        not np.isfinite(
            step
        )
        or step <= 0.0
    ):
        raise ValueError(
            "RK4 step must be a finite "
            "positive value"
        )

    k1 = np.asarray(
        function(
            t,
            state,
            *args,
        ),
        dtype=float,
    )

    k2 = np.asarray(
        function(
            t
            + 0.5
            * step,
            state
            + 0.5
            * step
            * k1,
            *args,
        ),
        dtype=float,
    )

    k3 = np.asarray(
        function(
            t
            + 0.5
            * step,
            state
            + 0.5
            * step
            * k2,
            *args,
        ),
        dtype=float,
    )

    k4 = np.asarray(
        function(
            t
            + step,
            state
            + step
            * k3,
            *args,
        ),
        dtype=float,
    )

    for name, derivative in (
        (
            "k1",
            k1,
        ),
        (
            "k2",
            k2,
        ),
        (
            "k3",
            k3,
        ),
        (
            "k4",
            k4,
        ),
    ):
        if (
            derivative.shape
            != state.shape
        ):
            raise ValueError(
                f"{name} shape mismatch: "
                f"expected {state.shape}, "
                f"got {derivative.shape}"
            )

        if not np.all(
            np.isfinite(
                derivative
            )
        ):
            raise FloatingPointError(
                "Non-finite derivative "
                f"detected in {name}"
            )

    next_state = (
        state
        + (
            step
            / 6.0
        )
        * (
            k1
            + 2.0
            * k2
            + 2.0
            * k3
            + k4
        )
    )

    if not np.all(
        np.isfinite(
            next_state
        )
    ):
        raise FloatingPointError(
            "Non-finite RK4 state "
            "detected"
        )

    return next_state


def bloch_rhs(
    t: float,
    s: np.ndarray,
    Omega: float,
    gamma: float,
    delta: float,
) -> np.ndarray:
    """Return the driven dissipative Bloch-system derivative."""

    del t

    state = np.asarray(
        s,
        dtype=float,
    )

    if state.shape != (
        3,
    ):
        raise ValueError(
            "Bloch state must have "
            "shape (3,)"
        )

    if not np.all(
        np.isfinite(
            state
        )
    ):
        raise ValueError(
            "Bloch state must contain "
            "only finite values"
        )

    Omega_value = float(
        Omega
    )

    gamma_value = float(
        gamma
    )

    delta_value = float(
        delta
    )

    if not np.isfinite(
        Omega_value
    ):
        raise ValueError(
            "Omega must be finite"
        )

    if (
        not np.isfinite(
            gamma_value
        )
        or gamma_value <= 0.0
    ):
        raise ValueError(
            "gamma must be a finite "
            "positive value"
        )

    if not np.isfinite(
        delta_value
    ):
        raise ValueError(
            "delta must be finite"
        )

    sx, sy, sz = state

    T1 = (
        1.0
        / gamma_value
    )

    T2 = (
        2.0
        * T1
    )

    dsx = (
        -sx
        / T2
        + delta_value
        * sy
    )

    dsy = (
        -sy
        / T2
        - delta_value
        * sx
        + Omega_value
        * sz
    )

    dsz = (
        -(
            sz
            + 1.0
        )
        / T1
        - Omega_value
        * sy
    )

    derivative = np.array(
        [
            dsx,
            dsy,
            dsz,
        ],
        dtype=float,
    )

    if not np.all(
        np.isfinite(
            derivative
        )
    ):
        raise FloatingPointError(
            "Non-finite Bloch derivative "
            "detected"
        )

    return derivative


def steady_state_bloch(
    Omega: float,
    gamma: float,
    delta: float,
) -> np.ndarray:
    """Solve the stationary state of the linear dissipative Bloch system."""

    Omega_value = float(
        Omega
    )

    gamma_value = float(
        gamma
    )

    delta_value = float(
        delta
    )

    if not np.isfinite(
        Omega_value
    ):
        raise ValueError(
            "Omega must be finite"
        )

    if (
        not np.isfinite(
            gamma_value
        )
        or gamma_value <= 0.0
    ):
        raise ValueError(
            "gamma must be a finite "
            "positive value"
        )

    if not np.isfinite(
        delta_value
    ):
        raise ValueError(
            "delta must be finite"
        )

    T1 = (
        1.0
        / gamma_value
    )

    T2 = (
        2.0
        * T1
    )

    matrix = np.array(
        [
            [
                -1.0
                / T2,
                delta_value,
                0.0,
            ],
            [
                -delta_value,
                -1.0
                / T2,
                Omega_value,
            ],
            [
                0.0,
                -Omega_value,
                -1.0
                / T1,
            ],
        ],
        dtype=float,
    )

    source = np.array(
        [
            0.0,
            0.0,
            1.0
            / T1,
        ],
        dtype=float,
    )

    steady_state = np.linalg.solve(
        matrix,
        source,
    )

    if not np.all(
        np.isfinite(
            steady_state
        )
    ):
        raise FloatingPointError(
            "Non-finite stationary "
            "Bloch state detected"
        )

    return steady_state


def run(
    params: Params,
    out_csv: Path,
) -> dict[str, object]:
    """Integrate one trajectory and write the complete state history to CSV."""

    validated = (
        params.validated()
    )

    output = Path(
        out_csv
    ).expanduser().resolve()

    steps = int(
        math.floor(
            validated.T
            / validated.dt
        )
    )

    if steps <= 0:
        raise ValueError(
            "The selected T and dt "
            "produce no integration steps"
        )

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    t = 0.0

    state = (
        validated.s0.copy()
    )

    with output.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.writer(
            handle
        )

        writer.writerow(
            [
                "t",
                "sx",
                "sy",
                "sz",
            ]
        )

        for step_index in range(
            steps
            + 1
        ):
            if not np.all(
                np.isfinite(
                    state
                )
            ):
                raise FloatingPointError(
                    "Non-finite state "
                    "detected at "
                    f"step {step_index}"
                )

            writer.writerow(
                [
                    f"{t:.17g}",
                    f"{state[0]:.17g}",
                    f"{state[1]:.17g}",
                    f"{state[2]:.17g}",
                ]
            )

            if (
                step_index
                == steps
            ):
                break

            state = rk4_step(
                bloch_rhs,
                state,
                t,
                validated.dt,
                args=(
                    validated.Omega,
                    validated.gamma,
                    validated.delta,
                ),
            )

            t = (
                step_index
                + 1
            ) * validated.dt

    stationary = (
        steady_state_bloch(
            validated.Omega,
            validated.gamma,
            validated.delta,
        )
    )

    final_error = float(
        np.linalg.norm(
            state
            - stationary
        )
    )

    return {
        "output": output,
        "steps": steps,
        "rows": (
            steps
            + 1
        ),
        "final_time": t,
        "final_state": state.copy(),
        "stationary_state": stationary,
        "stationary_error_l2": final_error,
    }


def parse_gamma_ratios(
    text: str,
) -> tuple[float, ...]:
    """Parse a comma-separated list of positive gamma/Omega ratios."""

    raw_values = [
        item.strip()
        for item in text.split(
            ","
        )
        if item.strip()
    ]

    if not raw_values:
        raise argparse.ArgumentTypeError(
            "At least one gamma/Omega "
            "ratio is required"
        )

    try:
        ratios = tuple(
            float(
                item
            )
            for item
            in raw_values
        )

    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "gamma ratios must be numeric"
        ) from exc

    if any(
        not np.isfinite(
            value
        )
        or value <= 0.0
        for value
        in ratios
    ):
        raise argparse.ArgumentTypeError(
            "gamma ratios must be finite "
            "positive values"
        )

    return ratios


def build_output_name(
    Omega: float,
    gamma_ratio: float,
    stamp: str,
) -> str:
    """Return a stable CSV filename for one trajectory."""

    safe_stamp = "".join(
        character
        for character in stamp
        if (
            character.isalnum()
            or character
            in (
                "-",
                "_",
            )
        )
    )

    if not safe_stamp:
        raise ValueError(
            "stamp must contain at least "
            "one safe filename character"
        )

    return (
        f"bloch_Omega{Omega:g}_"
        f"gammaOverOmega{gamma_ratio:g}_"
        f"stamp{safe_stamp}.csv"
    )


def generate_trajectories(
    Omega: float,
    gamma_ratios: Sequence[float],
    delta: float,
    periods: float,
    dt: float,
    s0: np.ndarray,
    output_dir: Path,
    stamp: str,
) -> list[dict[str, object]]:
    """Generate one trajectory for each gamma/Omega ratio."""

    Omega_value = float(
        Omega
    )

    periods_value = float(
        periods
    )

    dt_value = float(
        dt
    )

    delta_value = float(
        delta
    )

    if (
        not np.isfinite(
            Omega_value
        )
        or Omega_value <= 0.0
    ):
        raise ValueError(
            "Omega must be a finite "
            "positive value"
        )

    if (
        not np.isfinite(
            periods_value
        )
        or periods_value <= 0.0
    ):
        raise ValueError(
            "periods must be a finite "
            "positive value"
        )

    if (
        not np.isfinite(
            dt_value
        )
        or dt_value <= 0.0
    ):
        raise ValueError(
            "dt must be a finite "
            "positive value"
        )

    if not np.isfinite(
        delta_value
    ):
        raise ValueError(
            "delta must be finite"
        )

    ratio_values = tuple(
        float(
            value
        )
        for value
        in gamma_ratios
    )

    if not ratio_values:
        raise ValueError(
            "At least one gamma/Omega "
            "ratio is required"
        )

    if any(
        not np.isfinite(
            value
        )
        or value <= 0.0
        for value
        in ratio_values
    ):
        raise ValueError(
            "gamma/Omega ratios must be "
            "finite positive values"
        )

    initial_state = np.asarray(
        s0,
        dtype=float,
    )

    if initial_state.shape != (
        3,
    ):
        raise ValueError(
            "s0 must contain exactly "
            "three components"
        )

    if not np.all(
        np.isfinite(
            initial_state
        )
    ):
        raise ValueError(
            "s0 must contain only "
            "finite values"
        )

    output_directory = Path(
        output_dir
    ).expanduser().resolve()

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    T = (
        periods_value
        * (
            2.0
            * math.pi
            / Omega_value
        )
    )

    results: list[
        dict[
            str,
            object,
        ]
    ] = []

    for gamma_ratio in (
        ratio_values
    ):
        gamma = (
            gamma_ratio
            * Omega_value
        )

        params = Params(
            Omega=Omega_value,
            gamma=gamma,
            delta=delta_value,
            T=T,
            dt=dt_value,
            s0=initial_state,
        )

        output_name = (
            build_output_name(
                Omega=Omega_value,
                gamma_ratio=(
                    gamma_ratio
                ),
                stamp=stamp,
            )
        )

        result = run(
            params=params,
            out_csv=(
                output_directory
                / output_name
            ),
        )

        result[
            "gamma_ratio"
        ] = gamma_ratio

        result[
            "gamma"
        ] = gamma

        results.append(
            result
        )

    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate deterministic "
            "dissipative Bloch trajectories "
            "for the repository quasi-TWA demo"
        )
    )

    parser.add_argument(
        "--Omega",
        type=float,
        default=1.0,
        help=(
            "Coherent drive frequency"
        ),
    )

    parser.add_argument(
        "--gamma-ratios",
        type=parse_gamma_ratios,
        default=DEFAULT_GAMMA_RATIOS,
        help=(
            "Comma-separated gamma/Omega ratios. "
            "Default: 0.1,0.2,0.5,1.0"
        ),
    )

    parser.add_argument(
        "--delta",
        type=float,
        default=0.0,
        help=(
            "Drive detuning"
        ),
    )

    parser.add_argument(
        "--periods",
        type=float,
        default=20.0,
        help=(
            "Simulation duration "
            "in drive periods"
        ),
    )

    parser.add_argument(
        "--dt",
        type=float,
        default=0.0025,
        help=(
            "Fixed RK4 integration step"
        ),
    )

    parser.add_argument(
        "--initial-sx",
        type=float,
        default=0.0,
    )

    parser.add_argument(
        "--initial-sy",
        type=float,
        default=0.0,
    )

    parser.add_argument(
        "--initial-sz",
        type=float,
        default=-1.0,
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_LOGS_DIR,
        help=(
            "CSV output directory. "
            "Default: "
            "rpu_core/twa_demo/logs"
        ),
    )

    parser.add_argument(
        "--stamp",
        type=str,
        default=None,
        help=(
            "Filename stamp. "
            "Default: current local time. "
            "Use a fixed value for "
            "deterministic CI filenames."
        ),
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    stamp = (
        args.stamp
        if args.stamp
        is not None
        else time.strftime(
            "%Y%m%d_%H%M%S"
        )
    )

    initial_state = np.array(
        [
            args.initial_sx,
            args.initial_sy,
            args.initial_sz,
        ],
        dtype=float,
    )

    results = (
        generate_trajectories(
            Omega=args.Omega,
            gamma_ratios=(
                args.gamma_ratios
            ),
            delta=args.delta,
            periods=args.periods,
            dt=args.dt,
            s0=initial_state,
            output_dir=(
                args.output_dir
            ),
            stamp=stamp,
        )
    )

    for result in results:
        output = result[
            "output"
        ]

        gamma_ratio = result[
            "gamma_ratio"
        ]

        rows = result[
            "rows"
        ]

        stationary_error = result[
            "stationary_error_l2"
        ]

        print(
            f"[ok] gamma/Omega="
            f"{gamma_ratio:g} "
            f"rows={rows} "
            f"stationary_error_l2="
            f"{stationary_error:.6e}"
        )

        print(
            f"[ok] written "
            f"{output}"
        )

    print(
        f"[ok] generated "
        f"{len(results)} trajectories"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
