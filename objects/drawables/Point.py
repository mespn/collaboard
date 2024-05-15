from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float