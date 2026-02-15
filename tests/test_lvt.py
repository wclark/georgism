import pytest

from georgism.lvt import (
    LVTInputError,
    LandParcel,
    calculate_annual_lvt,
    calculate_monthly_lvt,
    portfolio_annual_lvt,
)


def test_calculate_annual_lvt() -> None:
    assert calculate_annual_lvt(500_000, 0.04) == 20_000


def test_calculate_monthly_lvt() -> None:
    assert calculate_monthly_lvt(120_000, 0.1) == 1_000


def test_land_parcel_annual_lvt() -> None:
    parcel = LandParcel(land_value=300_000, improvement_value=150_000, name="A")
    assert parcel.annual_lvt(0.03) == 9_000


def test_total_property_value() -> None:
    parcel = LandParcel(land_value=200_000, improvement_value=80_000)
    assert parcel.total_property_value == 280_000


def test_portfolio_annual_lvt() -> None:
    parcels = [LandParcel(100_000), LandParcel(250_000), LandParcel(50_000)]
    assert portfolio_annual_lvt(parcels, 0.05) == 20_000


@pytest.mark.parametrize("bad_rate", [-0.01, 1.5])
def test_invalid_rates_raise(bad_rate: float) -> None:
    with pytest.raises(LVTInputError):
        calculate_annual_lvt(100_000, bad_rate)


def test_negative_land_value_raises() -> None:
    with pytest.raises(LVTInputError):
        calculate_annual_lvt(-1, 0.05)
