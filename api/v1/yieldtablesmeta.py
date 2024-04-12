from typing import List

from fastapi import APIRouter, HTTPException

from api.models.exceptions import HTTPNotFoundError
from openyieldtables.models.yieldtable import YieldTableMeta
from openyieldtables.yieldtables import (
    get_yield_table_meta,
    get_yield_tables_meta,
)

router = APIRouter(
    prefix="/v1/yield-tables-meta",
    tags=["YieldTablesMeta"],
)


@router.get("/", response_model=List[YieldTableMeta])
def read_yield_tables_meta():
    return get_yield_tables_meta()


@router.get(
    "/{yield_table_id}",
    response_model=YieldTableMeta,
    responses={
        404: {
            "description": "Yield table not found",
            "model": HTTPNotFoundError,
        }
    },
)
def read_yield_table_meta(yield_table_id: int):
    try:
        return get_yield_table_meta(yield_table_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail={
                "message": f"Yield table with ID {yield_table_id} not found."
            },
        )
