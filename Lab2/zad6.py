import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


def filtr(filtrowane: dict, maska: dict) -> dict:
    Filtr = {}
    for k, v in filtrowane.items():
        czyPasuje = True
        for n, m in maska.items():
            if m[0] == "<":
                if not v[n] < m[1]:
                    czyPasuje = False
            elif m[0] == ">":
                if not v[n] > m[1]:
                    czyPasuje = False
            elif m[0] == "=":
                if not v[n] == m[1]:
                    czyPasuje = False
        if czyPasuje:
            Filtr[k] = v
    return Filtr


async def main():
    urlPorlamar = ("https://api.open-meteo.com/v1/forecast?latitude=10.9577&longitude=-63.8697&hourly=temperature_2m,"
                   "wind_speed_10m,relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=auto")
    urlMoroni = ("https://api.open-meteo.com/v1/forecast?latitude=-11.7022&longitude=43.2551&hourly=temperature_2m,"
                 "wind_speed_10m,relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=auto")
    urlHelsinki = ("https://api.open-meteo.com/v1/forecast?latitude=60.3172&longitude=24.9633&hourly=temperature_2m,"
                   "wind_speed_10m,relative_humidity_2m&current=temperature_2m,relative_humidity_2m&timezone=auto")
    temp = await asyncio.gather(fetch(urlPorlamar), fetch(urlMoroni), fetch(urlHelsinki))
    maska = {
        'temperature_2m': (">", 25),
        'relative_humidity_2m': ("<", 80)
    }
    tempDict = dict(zip(["Porlamar", "Moroni", "Helsinki"], [temp[0]['current'],
                         temp[1]['current'], temp[2]['current']]))
    tempFiltr = filtr(tempDict, maska)
    return tempFiltr

if __name__ == "__main__":
    test = asyncio.run(main())
    print(test)