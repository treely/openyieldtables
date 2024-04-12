from fastapi import APIRouter, HTTPException

from api.models.exceptions import HTTPNotFoundError
from openyieldtables.models.yieldtable import YieldTable
from openyieldtables.yieldtables import get_yield_table_data

router = APIRouter(
    prefix="/v1/yield-tables",
    tags=["YieldTables"],
)


@router.get(
    "/{yield_table_id}",
    response_model=YieldTable,
    responses={
        404: {
            "description": "Yield table not found",
            "model": HTTPNotFoundError,
        }
    },
)
def read_yield_table_data(yield_table_id: int):
    try:
        return get_yield_table_data(yield_table_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail={
                "message": f"Yield table with ID {yield_table_id} not found."
            },
        )
