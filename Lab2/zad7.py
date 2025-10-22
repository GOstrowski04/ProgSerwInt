import aiohttp
import asyncio
import datetime

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def main() -> None:
    plik = open("test.jpg", "wb")
    plik.write(await fetch("https://i.pinimg.com/736x/05/b4/fb/05b4fbc3f169175e6deb97b3977175b6.jpg"))
    plik.close()

if __name__ == "__main__":
    asyncio.run(main())