import aiohttp

from typing import Iterable

from zadanie1.api.utils import consts
from zadanie1.core.repositories.icomment import ICommentRepository
from zadanie1.core.domain.comment import Comment
from zadanie1.infrastructure.repositories.db import comments


class CommentMockRepository(ICommentRepository):
    async def get_all_comments(self) -> Iterable[Comment]:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        return parsed_params

    async def save_comments(self, comments: Iterable[Comment]) -> None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        comments.clear()
        comments.extend(parsed_params)

    async def get_by_name(self, name_fragment: str) -> Iterable[Comment]:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        return list(filter(lambda x: name_fragment in x.name, parsed_params))

    async def get_by_body(self, body_fragment: str) -> Iterable[Comment]:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        return list(filter(lambda x: body_fragment in x.body, parsed_params))

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_COMMENTS_URL) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[Comment]:
        return [Comment(postId=record.get("postId"), name=record.get("name"), body=record.get("body"),
                email = record.get("email"), id=record.get("id")) for record in params]