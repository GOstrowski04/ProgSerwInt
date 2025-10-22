

from typing import Iterable

from zadanie1.core.domain.post import Post, PostIn
from zadanie1.core.repositories.ipost import IPostRepository
from zadanie1.infrastructure.services.ipost import IPostService


class PostService(IPostService):
    """A class implementing the post service."""

    _repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        """The initializer of the 'post service'.

        Args:
            repository (IPostRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all(self) -> Iterable[Post]:
        """ The method getting all posts from the repository

        Returns:
             Iterable[Post]: All posts.
         """
        return await self._repository.get_all_posts()

    async def get_by_title(self, title_fragment: str) -> Iterable[Post]:
        """The method getting posts by fragment of title.

        Args:
            title_fragment (str): The fragment of the title.

        Returns:
            Iterable[Post]: Posts with the fragment in the title.
        """
        return await self._repository.get_by_title(title_fragment)

    async def get_by_body(self, body_fragment: str) -> Iterable[Post]:
        """The method getting posts by fragment of body.

        Args:
            body_fragment (str): The fragment of the body.
        Returns:
            Iterable[Post]: Posts with the fragment in the body.
        """
        return await self._repository.get_by_body(body_fragment)
