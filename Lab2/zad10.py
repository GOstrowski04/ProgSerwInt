import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = ("https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m,wind_speed_10m,"
           "relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=Europe%2FBerlin")
    temp = await fetch(url)
    processedTemperature = {
        'latitude': temp['latitude'],
        'longitude': temp['longitude'],
        'timezone': temp['timezone_abbreviation'],
        'units': temp['hourly_units'],
        'hourly': temp['hourly']
    }
    plik = open("zadanie10.txt", "w")
    plik.write(str(processedTemperature))
    plik.close()

if __name__ == "__main__":
    asyncio.run(main())