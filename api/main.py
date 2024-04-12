from fastapi import FastAPI

from api.v1 import yieldtables, yieldtablesmeta

app = FastAPI(title="openyieldtables API")


@app.get("/", include_in_schema=False)
def read_root():
    return {
        "message": "Welcome to the openyieldtables API! Please refer to the "
        "documentation at /docs."
    }


app.include_router(yieldtablesmeta.router)
app.include_router(yieldtables.router)
