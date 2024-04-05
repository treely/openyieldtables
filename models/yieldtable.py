from typing import List, Optional

from pydantic import BaseModel


class YieldTableMeta(BaseModel):
    id: int
    name: str
    tree_species_id: Optional[int] = None
    name_short: Optional[str] = None
    country_codes: List[str]
    type: Optional[str] = None
    assortment_table: Optional[int] = None
    weight: Optional[int] = None
    source: str
    active: Optional[bool] = None
    yield_value_step: Optional[float] = None
    age_step: Optional[int] = None
    age_min: Optional[int] = None
    age_max: Optional[int] = None
    missing_columns: Optional[List[str]] = None
    available_columns: List[str]


class YieldClassRow(BaseModel):
    age: int
    dominant_height: Optional[float] = None
    middle_height: Optional[float] = None
    diameter: Optional[float] = None
    taper: Optional[float] = None
    trees_per_ha: Optional[float] = None
    area: Optional[float] = None
    volume_per_ha: Optional[float] = None
    mean_volume_growth_per_ha: Optional[float] = None
    total_volume_per_ha: Optional[float] = None
    annual_volume_grow_per_ha: Optional[float] = None
    mean_total_growth_per_ha: Optional[float] = None


class YieldClass(BaseModel):
    yield_value: int
    rows: List[YieldClassRow]


class YieldTableData(BaseModel):
    yield_classes: List[YieldClass]


class YieldTable(YieldTableMeta):
    data: List[YieldTableData]
