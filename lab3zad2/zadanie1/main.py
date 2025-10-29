from dependency_injector.wiring import Provide

import asyncio

from conainer import Container
from zadanie1.infrastructure.services.ipost import IPostService
from zadanie1.infrastructure.services.icomment import ICommentService
from zadanie1.infrastructure.repositories.db import *


async def main(
        post_service: IPostService = Provide[Container.post_service],
        comment_service: ICommentService = Provide[Container.comment_service],
) -> None:
    await post_service.save_posts(posts)
    await comment_service.save_comments(comments)
    print(posts)
    print(comments)
if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    asyncio.run(main())