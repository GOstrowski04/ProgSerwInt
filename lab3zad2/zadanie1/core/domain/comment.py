from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CommentIn(BaseModel):
    postId: int
    email: str
    name: str
    body: str
    access_time: datetime = datetime.now()

class Comment(CommentIn):
    id: int
