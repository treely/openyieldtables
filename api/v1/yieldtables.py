from fastapi import APIRouter, HTTPException, Request
import yaml

from api.models.exceptions import HTTPNotFoundError
from api.v1.send_response import send_response
from openyieldtables.models.yieldtable import YieldTable
from openyieldtables.yieldtables import get_yield_table

router = APIRouter(
    prefix="/v1/yield-tables",
    tags=["YieldTables"],
)

with open("mkdocs.yml", "r") as file:
    docs = yaml.safe_load(file)


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
def read_yield_table_data(yield_table_id: int, request: Request):
    try:
        return send_response(
            get_yield_table(yield_table_id),
            "yield-table.html",
            request,
            docs["extra"]["yield_tables"],
        )
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail={
                "message": f"Yield table with ID {yield_table_id} not found."
            },
        )
