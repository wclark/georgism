# georgism

A Python package for modeling Georgist economics, beginning with practical Land Value Tax (LVT) calculators.

## What is included now

- Core LVT calculations from assessed land value and tax rates.
- A small `LandParcel` model to evaluate single parcels.
- Portfolio helpers to aggregate parcel-level LVT liabilities.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

```python
from georgism import LandParcel, calculate_annual_lvt

annual_tax = calculate_annual_lvt(land_value=400_000, lvt_rate=0.05)
print(annual_tax)  # 20000.0

parcel = LandParcel(land_value=250_000, improvement_value=120_000, name="Lot A")
print(parcel.annual_lvt(0.04))  # 10000.0
```

## Next roadmap ideas

- Progressive or tiered LVT schedules.
- Time-series simulation of land values and rental capture.
- Incidence and welfare analysis helpers.
- City-scale parcel datasets and scenario tooling.
