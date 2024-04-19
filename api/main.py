from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

from api.v1 import yieldtables, yieldtablesmeta

app = FastAPI(title="openyieldtables API")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root():
    return FileResponse("api/static/index.html")


@app.get("/health/readiness", include_in_schema=False)
def readiness():
    return {"status": "ok"}


@app.get("/health/liveness", include_in_schema=False)
def liveness():
    return {"status": "ok"}


app.include_router(yieldtablesmeta.router)
app.include_router(yieldtables.router)
