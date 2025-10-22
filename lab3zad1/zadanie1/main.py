from dependency_injector.wiring import Provide

import asyncio

from conainer import Container
from zadanie1.infrastructure.services.ipost import IPostService
from zadanie1.api.utils import consts


async def main(
        service: IPostService = Provide(Container.service),
) -> None:
    wszystkie = await service.get_all()
    filteredByTitle= await service.get_by_title("facere")
    filteredByBody = await service.get_by_body("odio")
    print(wszystkie)
    print(filteredByTitle)
    print(filteredByBody)

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())