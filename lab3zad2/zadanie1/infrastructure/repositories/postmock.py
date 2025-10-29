import aiohttp

from datetime import datetime
from typing import Iterable

from zadanie1.api.utils import consts
from zadanie1.core.repositories.ipost import IPostRepository
from zadanie1.core.domain.post import Post
from zadanie1.infrastructure.repositories.db import posts


class PostMockRepository(IPostRepository):
    async def get_all_posts(self) -> Iterable[Post]:
        for post in posts:
            post.access_time = datetime.now()
        return posts

    async def save_posts(self, posts: Iterable[Post]) -> None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        posts.clear()
        posts.extend(parsed_params)

    async def get_by_title(self, title_fragment: str) -> Iterable[Post]:
        filtered = list(filter(lambda x: title_fragment in x.title, posts))
        for post in filtered:
            post.access_time = datetime.now()
        return filtered

    async def get_by_body(self, body_fragment: str) -> Iterable[Post]:
        filtered = list(filter(lambda x: body_fragment in x.body, posts))
        for post in filtered:
            post.access_time = datetime.now()
        return filtered

    async def sort_by_access_time(self) -> Iterable[Post]:
        return list(sorted(posts, key=lambda x: x.access_time, reverse=True))

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_SENSOR_URL) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[Post]:
        return [Post(user_id=record.get("userId"), title=record.get("title"), body=record.get("body"),
                id=record.get("id")) for record in params]