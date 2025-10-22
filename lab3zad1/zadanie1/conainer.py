from dependency_injector import containers, providers

from zadanie1.infrastructure.repositories.postmock import PostMockRepository
from zadanie1.infrastructure.services.post import PostService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repository = providers.Singleton(
        PostMockRepository,
    )
    service = providers.Factory(
        PostService,
        repository=repository,
    )