import aiohttp
import asyncio
import datetime

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = ("https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m,wind_speed_10m,"
           "relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=Europe%2FBerlin")
    users = await fetch(url)
    print(users['current'])

if __name__ == "__main__":
    asyncio.run(main())
    print(datetime.datetime.now().hour+1)