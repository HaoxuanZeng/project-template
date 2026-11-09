"""Parameters that identify a single simulation."""

from dataclasses import dataclass


@dataclass(frozen=True)
class StatePoint:
    n: int
    epsilon: float
    sigma: float
    temperature: float
    number_density: float
    replicate: int
