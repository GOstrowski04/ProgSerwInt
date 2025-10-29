from dependency_injector import containers, providers

from zadanie1.infrastructure.repositories.commentmock import CommentMockRepository
from zadanie1.infrastructure.repositories.postmock import PostMockRepository
from zadanie1.infrastructure.services.comment import CommentService
from zadanie1.infrastructure.services.post import PostService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    post_repository = providers.Singleton(
        PostMockRepository,
    )
    comment_repository = providers.Singleton(
        CommentMockRepository,
    )
    post_service = providers.Factory(
        PostService,
        repository=post_repository,
    )
    comment_service = providers.Factory(
        CommentService,
        repository=comment_repository,
    )