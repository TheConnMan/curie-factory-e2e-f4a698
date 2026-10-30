"""Conversion table and the one function the CLI calls."""

from __future__ import annotations

LENGTH_TO_METERS = {
    "m": 1.0,
    "km": 1000.0,
    "mi": 1609.344,
    "ft": 0.3048,
}

TEMPERATURE = {"c", "f", "k"}

# Lowest valid value in each temperature unit (absolute zero).
ABSOLUTE_ZERO = {"c": -273.15, "f": -459.67, "k": 0.0}


class UnknownUnit(ValueError):
    """Raised when a unit is not in the table."""


def convert(value: float, src: str, dst: str) -> float:
    """Convert ``value`` from unit ``src`` to unit ``dst``.

    Temperature and length units cannot be mixed.
    """
    src = src.lower()
    dst = dst.lower()
    if src in TEMPERATURE and dst in TEMPERATURE:
        return _convert_temperature(value, src, dst)
    if src in LENGTH_TO_METERS and dst in LENGTH_TO_METERS:
        meters = value * LENGTH_TO_METERS[src]
        return meters / LENGTH_TO_METERS[dst]
    if src not in TEMPERATURE and src not in LENGTH_TO_METERS:
        raise UnknownUnit(src)
    if dst not in TEMPERATURE and dst not in LENGTH_TO_METERS:
        raise UnknownUnit(dst)
    raise ValueError(f"cannot convert {src} to {dst}")


def _convert_temperature(value: float, src: str, dst: str) -> float:
    if value < ABSOLUTE_ZERO[src]:
        raise ValueError(f"{value} {src} is below absolute zero")
    if src == dst:
        return value
    if src == "c" and dst == "f":
        return value * 9 / 5 + 32
    if src == "f" and dst == "c":
        return (value - 32) * 5 / 9
    if src == "k":
        celsius = value - 273.15
        return celsius if dst == "c" else celsius * 9 / 5 + 32
    # dst is "k"
    celsius = value if src == "c" else (value - 32) * 5 / 9
    return celsius + 273.15
