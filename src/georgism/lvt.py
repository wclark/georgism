"""Land Value Tax (LVT) calculators and supporting parcel models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class LVTInputError(ValueError):
    """Raised when LVT inputs are invalid."""


def _validate_non_negative(name: str, value: float) -> None:
    if value < 0:
        raise LVTInputError(f"{name} must be non-negative, got {value}.")


def _validate_rate(rate: float) -> None:
    if not 0 <= rate <= 1:
        raise LVTInputError(f"lvt_rate must be between 0 and 1, got {rate}.")


def calculate_annual_lvt(land_value: float, lvt_rate: float) -> float:
    """Calculate annual land value tax.

    Args:
        land_value: Assessed market value of land only.
        lvt_rate: Tax rate as a decimal (e.g., 0.05 for 5%).

    Returns:
        Annual LVT liability.
    """

    _validate_non_negative("land_value", land_value)
    _validate_rate(lvt_rate)
    return land_value * lvt_rate


def calculate_monthly_lvt(land_value: float, lvt_rate: float) -> float:
    """Calculate monthly land value tax from annual liability."""

    return calculate_annual_lvt(land_value=land_value, lvt_rate=lvt_rate) / 12


@dataclass(frozen=True)
class LandParcel:
    """Representation of a parcel for Georgist tax modeling."""

    land_value: float
    improvement_value: float = 0.0
    name: str | None = None

    def annual_lvt(self, lvt_rate: float) -> float:
        """Compute annual LVT for this parcel."""

        return calculate_annual_lvt(self.land_value, lvt_rate)

    @property
    def total_property_value(self) -> float:
        """Land + improvements for comparison analyses."""

        _validate_non_negative("land_value", self.land_value)
        _validate_non_negative("improvement_value", self.improvement_value)
        return self.land_value + self.improvement_value


def portfolio_annual_lvt(parcels: Iterable[LandParcel], lvt_rate: float) -> float:
    """Aggregate annual LVT for a collection of parcels."""

    _validate_rate(lvt_rate)
    return sum(parcel.annual_lvt(lvt_rate) for parcel in parcels)
