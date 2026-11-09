"""Implement workflow actions."""

import argparse
import logging
import sys
from pathlib import Path

import signac

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from state_point import StatePoint


def simulate(*jobs) -> None:
    for job in jobs:
        state_point = StatePoint(**dict(job.sp))

        logging.info(
            "Loaded `%s`: n=%d, temperature=%s",
            job.path,
            state_point.n,
            state_point.temperature,
        )

        # Initialize and run your simulation using state_point.
        # Write job-specific files under job.path.


def main() -> None:
    actions = {"simulate": simulate}

    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True, choices=actions)
    parser.add_argument("directories", nargs="+")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )

    # Explicitly open data/, not the project in workflow/.
    project = signac.get_project(
        path=str(ROOT / "data"),
        search=False,
    )

    jobs = [project.open_job(id=directory) for directory in args.directories]

    actions[args.action](*jobs)


if __name__ == "__main__":
    main()
