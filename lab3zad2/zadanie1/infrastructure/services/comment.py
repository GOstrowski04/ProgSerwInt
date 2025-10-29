

from typing import Iterable

from zadanie1.core.domain.comment import Comment, CommentIn
from zadanie1.core.repositories.icomment import ICommentRepository
from zadanie1.infrastructure.services.icomment import ICommentService


class CommentService(ICommentService):
    """A class implementing the comment service."""

    _repository: ICommentRepository

    def __init__(self, repository: ICommentRepository) -> None:
        """The initializer of the 'comment service'.

        Args:
            repository (ICommentRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all_comments(self) -> Iterable[Comment]:
        """ The method getting all comments from the repository

        Returns:
             Iterable[Comment]: All comments.
         """
        return await self._repository.get_all_comments()

    async def save_comments(self, comments: Iterable[Comment]) -> None:
        """The method saving all comments from the repository"""
        await self._repository.save_comments(comments)

    async def get_by_name(self, name_fragment: str) -> Iterable[Comment]:
        """The method getting comments by fragment of name.

        Args:
            name_fragment (str): The fragment of the name.

        Returns:
            Iterable[Comment]: Comments with the fragment in the name.
        """
        return await self._repository.get_by_name(name_fragment)

    async def get_by_body(self, body_fragment: str) -> Iterable[Comment]:
        """The method getting comments by fragment of body.

        Args:
            body_fragment (str): The fragment of the body.
        Returns:
            Iterable[Comment]: Comments with the fragment in the body.
        """
        return await self._repository.get_by_body(body_fragment)
