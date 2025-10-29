from abc import ABC, abstractmethod
from typing import Iterable

from zadanie1.core.domain.comment import Comment


class ICommentRepository(ABC):
    @abstractmethod
    async def get_all_comments(self) -> Iterable[Comment]:
        """The abstract getting all comments from the data storage.

        Returns:
            Iterable[comment]: comments in the data storage.
        """
    @abstractmethod
    async def save_comments(self, comments: Iterable[Comment]) -> None:
        """The abstract saving all comments to the data storage.

        """
    @abstractmethod
    async def get_by_name(self, name_fragment: str) -> Iterable[Comment]:
        """The abstract getting comments by fragment of name.

        Returns:
            Iterable[comment]: comments in the data storage.
        """
    @abstractmethod
    async def get_by_body(self, body_fragment: str) -> Iterable[Comment]:
        """The abstract getting comments by fragment of body.

        Returns:
        Iterable[comment]: comments in the data storage.
        """
