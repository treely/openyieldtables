from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request
import pandas as pd
import yaml

from api.dependencies import get_yield_tables_meta_dep
from api.models.exceptions import HTTPNotFoundError
from api.v1.send_response import send_response
from openyieldtables.models.yieldtable import YieldTableMeta
from openyieldtables.yieldtables import (
    get_yield_table_meta_from_df,
    get_yield_tables_meta_from_df,
)

router = APIRouter(
    prefix="/v1/yield-tables-meta",
    tags=["YieldTablesMeta"],
)

with open("mkdocs.yml", "r") as file:
    docs = yaml.safe_load(file)


@router.get("/", response_model=List[YieldTableMeta])
def read_yield_tables_meta(
    request: Request,
    yield_tables_meta: pd.DataFrame = Depends(get_yield_tables_meta_dep),
):
    return send_response(
        get_yield_tables_meta_from_df(yield_tables_meta),
        "yield-tables-meta.html",
        request,
        None,
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
def read_yield_table_meta(
    yield_table_id: int,
    request: Request,
    yield_tables_meta: pd.DataFrame = Depends(get_yield_tables_meta_dep),
):
    try:
        return send_response(
            get_yield_table_meta_from_df(yield_table_id, yield_tables_meta),
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
