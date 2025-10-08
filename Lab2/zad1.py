import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://68e6851b21dd31f22cc5ffad.mockapi.io/api/v1/user"
    users = await fetch(url)
    print(users)


if __name__ == "__main__":
    asyncio.run(main())