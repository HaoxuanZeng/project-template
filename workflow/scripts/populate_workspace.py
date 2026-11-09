"""Populate the workspace."""

import sys
from dataclasses import asdict
from pathlib import Path

import signac

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "src"))

from state_point import StatePoint


def main() -> None:
    project = signac.init_project(path=str(ROOT / "data"))

    for temperature, replicate in [(1.0, 0), (1.0, 1), (0.7, 0)]:
        state_point = StatePoint(
            n=1_000,
            epsilon=1.0,
            sigma=1.0,
            temperature=temperature,
            number_density=0.4,
            replicate=replicate,
        )

        job = project.open_job(statepoint=asdict(state_point)).init()
        print(job.id)


if __name__ == "__main__":
    main()
