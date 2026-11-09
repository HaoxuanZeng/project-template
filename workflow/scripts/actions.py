"""Implement workflow actions."""

import argparse
import logging
import sys
from pathlib import Path

import signac

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "src"))

from state_point import StatePoint

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)


def simulate(*jobs) -> None:
    """Implement the simulation action."""
    for job in jobs:
        state_point = StatePoint(**dict(job.sp))

        varying_keys = sorted(project.detect_schema(exclude_const=True))

        summary = ", ".join(f"{key}={job.sp[key]}" for key in varying_keys)

        logger.info("%s", summary)

        # Initialize and run your simulation using state_point.
        # Write job-specific files under job.path.


if __name__ == "__main__":
    # Parse the command line arguments: python action.py --action <ACTION> [DIRECTORIES]
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True)
    parser.add_argument("directories", nargs="+")
    args = parser.parse_args()

    # Open the signac jobs
    project = signac.get_project(str(ROOT / "data"))
    jobs = [project.open_job(id=directory) for directory in args.directories]

    # Call the action
    globals()[args.action](*jobs)
