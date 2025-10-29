

from pydantic import BaseModel, ConfigDict


class CommentIn(BaseModel):
    postId: int
    email: str
    name: str
    body: str

class Comment(CommentIn):
    id: int
