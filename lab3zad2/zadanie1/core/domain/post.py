from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostIn(BaseModel):
    user_id: int
    title: str
    body: str
    access_time: datetime = datetime.now()

class Post(PostIn):
    id: int
