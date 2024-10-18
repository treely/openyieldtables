from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse

from api.dependencies import (
    df_manager,
    get_yield_tables_data_dep,
    get_yield_tables_meta_dep,
)
from api.v1 import yieldtables, yieldtablesmeta


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the yield tables data and meta data on app startup
    await df_manager.load_yield_tables_data()
    await df_manager.load_yield_tables_meta()
    yield
    # Clean up resources on app shutdown
    df_manager.yield_tables_df = None
    df_manager.yield_tables_meta_df = None


app = FastAPI(title="openyieldtables API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root():
    return FileResponse("api/static/index.html")


@app.get("/health/readiness", include_in_schema=False)
def readiness():
    return {"status": "ok"}


@app.get("/health/liveness", include_in_schema=False)
def liveness():
    return {"status": "ok"}


app.include_router(
    yieldtablesmeta.router,
    dependencies=[
        Depends(get_yield_tables_meta_dep),
    ],
)
app.include_router(
    yieldtables.router,
    dependencies=[
        Depends(get_yield_tables_data_dep),
        Depends(get_yield_tables_meta_dep),
    ],
)
