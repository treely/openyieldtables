from typing import Optional

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="api/templates")


def send_response(
    data: object, html_template: str, request: Request, docs: Optional[object]
):
    if "application/json" in request.headers.get("accept", ""):
        return data

    if docs:
        return templates.TemplateResponse(
            html_template, {"request": request, "data": data, "docs": docs}
        )
    return templates.TemplateResponse(
        html_template, {"request": request, "data": data}
    )
