from typing import List, Optional

from pydantic import BaseModel


class YieldTableMeta(BaseModel):
    id: int
    name: str
    country_codes: List[str]
    type: Optional[str] = None
    source: str
    link: Optional[str] = None
    yield_value_step: Optional[float] = None
    age_step: Optional[int] = None
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
