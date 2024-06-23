from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel


class TreeType(str, Enum):
    coniferous = "coniferous"
    deciduous = "deciduous"


class YieldTableMeta(BaseModel):
    id: int
    title: str
    country_codes: List[str]
    type: Optional[str] = None
    source: str
    link: Optional[str] = None
    yield_class_step: Optional[float] = None
    age_step: Optional[int] = None
    available_columns: List[str]
    tree_type: TreeType


class YieldClassRow(BaseModel):
    age: int
    dominant_height: Optional[float] = None
    average_height: Optional[float] = None
    dbh: Optional[float] = None
    taper: Optional[float] = None
    trees_per_ha: Optional[float] = None
    basal_area: Optional[float] = None
    volume_per_ha: Optional[float] = None
    average_annual_age_increment: Optional[float] = None
    total_growth_performance: Optional[float] = None
    current_annual_increment: Optional[float] = None
    mean_annual_increment: Optional[float] = None


class YieldClass(BaseModel):
    yield_class: Union[int, float]
    rows: List[YieldClassRow]


class YieldTableData(BaseModel):
    yield_classes: List[YieldClass]


class YieldTable(YieldTableMeta):
    data: YieldTableData
