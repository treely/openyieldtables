from typing import List

from fastapi import APIRouter, HTTPException, Request
import yaml

from api.models.exceptions import HTTPNotFoundError
from api.v1.send_response import send_response
from openyieldtables.models.yieldtable import YieldTableMeta
from openyieldtables.yieldtables import (
    get_yield_table_meta,
    get_yield_tables_meta,
)

router = APIRouter(
    prefix="/v1/yield-tables-meta",
    tags=["YieldTablesMeta"],
)

with open("mkdocs.yml", "r") as file:
    docs = yaml.safe_load(file)


@router.get("/", response_model=List[YieldTableMeta])
def read_yield_tables_meta(request: Request):
    return send_response(
        get_yield_tables_meta(), "yield-tables-meta.html", request, None
    )


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
def read_yield_table_meta(yield_table_id: int, request: Request):
    try:
        return send_response(
            get_yield_table_meta(yield_table_id),
            "yield-table-meta.html",
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
