import aiohttp

from datetime import datetime, timedelta
from typing import Iterable

from zadanie1.api.utils import consts
from zadanie1.core.repositories.icomment import ICommentRepository
from zadanie1.core.domain.comment import Comment
from zadanie1.infrastructure.repositories.db import comments


class CommentMockRepository(ICommentRepository):
    async def get_all_comments(self) -> Iterable[Comment]:
        now = datetime.now()
        filtered = list(filter(lambda x: (now - x.access_time).total_seconds() > 15, comments))
        filtered.clear()
        for comment in comments:
            comment.access_time = datetime.now()
        return comments

    async def save_comments(self, comments: Iterable[Comment]) -> None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        comments.clear()
        comments.extend(parsed_params)

    async def get_by_name(self, name_fragment: str) -> Iterable[Comment]:
        filtered = list(filter(lambda x: name_fragment in x.name, comments))
        for comment in filtered:
            comment.access_time = datetime.now()
        return filtered

    async def get_by_body(self, body_fragment: str) -> Iterable[Comment]:
        now = datetime.now()
        filtered = list(filter(lambda x: (now - x.access_time).total_seconds() > 15, comments))
        filtered.clear()
        filtered = list(filter(lambda x: body_fragment in x.body, comments))
        for comment in filtered:
            comment.access_time = datetime.now()
        return filtered

    async def sort_by_access_time(self) -> Iterable[Comment]:

        return list(sorted(comments, key=lambda x: x.access_time, reverse=True))

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_COMMENTS_URL) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[Comment]:
        return [Comment(postId=record.get("postId"), name=record.get("name"), body=record.get("body"),
                email = record.get("email"), id=record.get("id")) for record in params]