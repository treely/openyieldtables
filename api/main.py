from fastapi import FastAPI

from api.v1 import yieldtables, yieldtablesmeta

app = FastAPI(title="openyieldtables API")


@app.get("/", include_in_schema=False)
def read_root():
    return {
        "message": "Welcome to the openyieldtables API! Please refer to the "
        "documentation at /docs."
    }


@app.get("/health/readiness", include_in_schema=False)
def readiness():
    return {"status": "ok"}


@app.get("/health/liveness", include_in_schema=False)
def liveness():
    return {"status": "ok"}


app.include_router(yieldtablesmeta.router)
app.include_router(yieldtables.router)
