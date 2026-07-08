#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plot validated dissipative Bloch trajectories produced by the TWA demo."""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np


REQUIRED_COLUMNS = (
    "t",
    "sx",
    "sy",
    "sz",
)

DEFAULT_LOGS_DIR = (
    Path(__file__).resolve().parent
    / "rpu_core"
    / "twa_demo"
    / "logs"
)

DEFAULT_OUTPUT_NAME = "bloch_twa_results.png"


def load_csv(
    file_path: Path,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    """Load and validate one Bloch trajectory CSV file."""

    path = Path(
        file_path
    ).expanduser().resolve()

    if not path.is_file():
        raise FileNotFoundError(
            f"CSV file not found: {path}"
        )

    rows: list[
        tuple[
            float,
            float,
            float,
            float,
        ]
    ] = []

    with path.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        reader = csv.DictReader(
            handle
        )

        if reader.fieldnames is None:
            raise ValueError(
                f"CSV file has no header: {path}"
            )

        missing = [
            column
            for column in REQUIRED_COLUMNS
            if column
            not in reader.fieldnames
        ]

        if missing:
            raise ValueError(
                f"CSV file {path} is missing "
                f"required columns: "
                f"{', '.join(missing)}"
            )

        for line_number, row in enumerate(
            reader,
            start=2,
        ):
            try:
                values = tuple(
                    float(
                        row[column]
                    )
                    for column
                    in REQUIRED_COLUMNS
                )

            except (
                TypeError,
                ValueError,
            ) as exc:
                raise ValueError(
                    f"Invalid numeric value "
                    f"in {path} "
                    f"at line {line_number}"
                ) from exc

            if not np.all(
                np.isfinite(
                    values
                )
            ):
                raise ValueError(
                    f"Non-finite numeric value "
                    f"in {path} "
                    f"at line {line_number}"
                )

            rows.append(
                values
            )

    if not rows:
        raise ValueError(
            f"CSV file contains "
            f"no trajectory rows: {path}"
        )

    data = np.asarray(
        rows,
        dtype=float,
    )

    t, sx, sy, sz = data.T

    if (
        t.size > 1
        and np.any(
            np.diff(t) <= 0.0
        )
    ):
        raise ValueError(
            f"Time values must be "
            f"strictly increasing: {path}"
        )

    return (
        t,
        sx,
        sy,
        sz,
    )


def discover_csv_files(
    logs_dir: Path,
) -> list[Path]:
    """Return trajectory CSV files from the demo log directory."""

    directory = Path(
        logs_dir
    ).expanduser().resolve()

    if not directory.is_dir():
        raise FileNotFoundError(
            f"Logs directory not found: "
            f"{directory}"
        )

    files = sorted(
        path
        for path in directory.glob(
            "*.csv"
        )
        if path.is_file()
    )

    if not files:
        raise FileNotFoundError(
            f"No CSV trajectory files "
            f"found in: {directory}. "
            f"Run "
            f"rpu_core/twa_demo/"
            f"run_twa_demo.py first."
        )

    return files


def plot_results(
    files: Iterable[Path],
    output_path: Path | None = None,
    show: bool = True,
) -> Path:
    """
    Validate trajectories,
    plot <sigma_z>(t),
    and save a PNG artifact.
    """

    file_list = [
        Path(
            file_path
        )
        for file_path in files
    ]

    if not file_list:
        raise ValueError(
            "At least one CSV file "
            "is required"
        )

    output = (
        Path(
            output_path
        )
        .expanduser()
        .resolve()
        if output_path is not None
        else (
            file_list[0]
            .resolve()
            .parent
            / DEFAULT_OUTPUT_NAME
        )
    )

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    figure, axis = plt.subplots(
        figsize=(
            10,
            6,
        )
    )

    try:
        for file_path in file_list:
            (
                t,
                _,
                _,
                sz,
            ) = load_csv(
                file_path
            )

            axis.plot(
                t,
                sz,
                label=file_path.stem,
            )

        axis.set_xlabel(
            "Ωt"
        )

        axis.set_ylabel(
            "⟨σz⟩"
        )

        axis.set_title(
            "Bloch Dynamics — "
            "TWA Simulation"
        )

        axis.legend()

        axis.grid(
            True
        )

        figure.tight_layout()

        figure.savefig(
            output,
            dpi=160,
            bbox_inches="tight",
        )

        if show:
            plt.show()

    finally:
        plt.close(
            figure
        )

    return output


def default_show_mode() -> bool:
    """
    Show interactively when
    a graphical session is available.
    """

    if os.environ.get(
        "CI"
    ):
        return False

    backend = (
        plt.get_backend()
        .lower()
    )

    non_interactive_backends = (
        "agg",
        "pdf",
        "ps",
        "svg",
        "template",
    )

    if any(
        name in backend
        for name
        in non_interactive_backends
    ):
        return False

    if (
        os.name == "nt"
        or "macosx" in backend
    ):
        return True

    return bool(
        os.environ.get(
            "DISPLAY"
        )
        or os.environ.get(
            "WAYLAND_DISPLAY"
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate and plot dissipative "
            "Bloch trajectories generated by "
            "rpu_core/twa_demo/"
            "run_twa_demo.py"
        )
    )

    parser.add_argument(
        "--logs-dir",
        type=Path,
        default=DEFAULT_LOGS_DIR,
        help=(
            "Directory containing "
            "trajectory CSV files"
        ),
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=(
            "PNG output path. "
            "Default: "
            "<logs-dir>/"
            "bloch_twa_results.png"
        ),
    )

    show_group = (
        parser
        .add_mutually_exclusive_group()
    )

    show_group.add_argument(
        "--show",
        action="store_true",
        help=(
            "Force interactive display "
            "after saving the PNG"
        ),
    )

    show_group.add_argument(
        "--no-show",
        action="store_true",
        help=(
            "Disable interactive display "
            "for CI or headless execution"
        ),
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    logs_dir = (
        args.logs_dir
        .expanduser()
        .resolve()
    )

    files = discover_csv_files(
        logs_dir
    )

    output = (
        args.output
        .expanduser()
        .resolve()
        if args.output is not None
        else (
            logs_dir
            / DEFAULT_OUTPUT_NAME
        )
    )

    if args.show:
        show = True

    elif args.no_show:
        show = False

    else:
        show = default_show_mode()

    saved_path = plot_results(
        files=files,
        output_path=output,
        show=show,
    )

    print(
        f"[ok] validated "
        f"{len(files)} "
        f"CSV trajectory files"
    )

    print(
        f"[ok] saved "
        f"{saved_path}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
