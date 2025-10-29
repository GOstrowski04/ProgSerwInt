

from abc import ABC, abstractmethod
from typing import Iterable

from zadanie1.core.domain.post import Post


class IPostService(ABC):

    @abstractmethod
    async def get_all(self) -> Iterable[Post]:
        """ The method getting all posts from the repository

        Returns:
            Iterable[Post]: All posts.
        """
    @abstractmethod
    async def save_posts(self, posts: Iterable[Post]) -> None:
        """The abstract saving all posts from the data storage.
    """

    @abstractmethod
    async def get_by_title(self, title_fragment: str) -> Iterable[Post]:
        """The method getting posts by fragment of title.

        Args:
            title_fragment (str): The fragment of the title.

        Returns:
            Iterable[Post]: Posts with the fragment in the title.
        """

    @abstractmethod
    async def get_by_body(self, body_fragment: str) -> Iterable[Post]:
        """The method getting posts by fragment of body.

        Args:
            body_fragment (str): The fragment of the body.
        Returns:
            Iterable[Post]: Posts with the fragment in the body.
        """