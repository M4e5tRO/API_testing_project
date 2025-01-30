from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional


class BaseScheme(BaseModel):
    @field_validator("*")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class AuthScheme(BaseScheme):
    token: str
    user: str


class InfoScheme(BaseScheme):
    description: Optional[str] = None
    policy: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class BaseResponseScheme(BaseScheme):
    id: int
    info: InfoScheme
    tags: list
    text: str
    updated_by: str
    url: str


class GetAllMemesScheme(BaseScheme):
    data: list[BaseResponseScheme]


class PostScheme(BaseResponseScheme):
    pass


class GetMemeScheme(BaseResponseScheme):
    pass


class PutScheme(BaseResponseScheme):
    pass
