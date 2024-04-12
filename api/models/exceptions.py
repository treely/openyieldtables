from pydantic import BaseModel, ConfigDict


class Message(BaseModel):
    message: str


class HTTPNotFoundError(BaseModel):
    detail: Message

    model_config = ConfigDict(
        json_schema_extra={"example": {"detail": {"message": "string"}}}
    )
