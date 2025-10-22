

from pydantic import BaseModel, ConfigDict


class PostIn(BaseModel):
    user_id: int
    title: str
    body: str


class Post(PostIn):
    id: int

