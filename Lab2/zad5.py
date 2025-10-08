import aiohttp
import asyncio
import datetime

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    urlPorlamar = ("https://api.open-meteo.com/v1/forecast?latitude=10.9577&longitude=-63.8697&hourly=temperature_2m,"
                   "wind_speed_10m,relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=auto")
    urlMoroni = ("https://api.open-meteo.com/v1/forecast?latitude=-11.7022&longitude=43.2551&hourly=temperature_2m,"
                 "wind_speed_10m,relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=auto")
    urlHelsinki = ("https://api.open-meteo.com/v1/forecast?latitude=60.3172&longitude=24.9633&hourly=temperature_2m,"
                   "wind_speed_10m,relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=auto")
    users = await asyncio.gather(fetch(urlPorlamar), fetch(urlMoroni), fetch(urlHelsinki))
    print(users['current'])

if __name__ == "__main__":
    asyncio.run(main())
    print(datetime.datetime.now().hour+1)