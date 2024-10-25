from pydantic import BaseModel
from typing import Optional


class AuthScheme(BaseModel):
    token: str
    user: str


class InfoScheme(BaseModel):
    description: Optional[str] = None
    policy: Optional[str] = None


class BaseResponseScheme(BaseModel):
    id: int
    info: InfoScheme
    tags: list
    text: str
    updated_by: str
    url: str


class GetAllMemesScheme(BaseModel):
    data: list[BaseResponseScheme]


class PostScheme(BaseResponseScheme):
    pass


class GetMemeScheme(BaseResponseScheme):
    pass


class PutScheme(BaseResponseScheme):
    pass
