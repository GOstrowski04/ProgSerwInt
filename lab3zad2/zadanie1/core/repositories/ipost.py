

from abc import ABC, abstractmethod
from typing import Iterable

from zadanie1.core.domain.post import Post


class IPostRepository(ABC):
    @abstractmethod
    async def get_all_posts(self) -> Iterable[Post]:
        """The abstract getting all posts from the data storage.

        Returns:
            Iterable[Post]: Posts in the data storage.
        """
    @abstractmethod
    async def save_posts(self, posts: Iterable[Post]) -> None:
        """The abstract saving all posts from the data storage.
    """

    @abstractmethod
    async def get_by_title(self, title_fragment: str) -> Iterable[Post]:
        """The abstract getting posts by fragment of title.

        Returns:
            Iterable[Post]: Posts in the data storage.
        """
    @abstractmethod
    async def get_by_body(self, body_fragment: str) -> Iterable[Post]:
        """The abstract getting posts by fragment of body.

        Returns:
        Iterable[Post]: Posts in the data storage.
        """
