import aiohttp
import asyncio
import datetime

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urlWarsaw = ("https://api.open-meteo.com/v1/forecast?latitude=52.2298&longitude=21.0118&daily=temperature_2m_max,"
                 "temperature_2m_min&timezone=auto&forecast_days=3")
    urlKrakow = ("https://api.open-meteo.com/v1/forecast?latitude=50.0614&longitude=19.9366&daily=temperature_2m_max,"
                 "temperature_2m_min&timezone=auto&forecast_days=3")
    urlGdansk = ("https://api.open-meteo.com/v1/forecast?latitude=54.3523&longitude=18.6491&daily=temperature_2m_max,"
                 "temperature_2m_min&timezone=auto&forecast_days=3")
    temp = await asyncio.gather(fetch(urlWarsaw), fetch(urlKrakow), fetch(urlGdansk))
    tempDict = dict(zip(["Warsaw", "Krakow", "Gdansk"], [temp[0]['daily'],
                                                              temp[1]['daily'], temp[2]['daily']]))
    for n in tempDict.keys():
        avg = (tempDict[n]['temperature_2m_max'][1] + tempDict[n]['temperature_2m_min'][1]) / 2
        tempDict[n]['avgTomorrow'] = avg
    posortowane = dict(sorted(tempDict.items(), key=lambda x: x[1]['avgTomorrow'], reverse=True))
    return posortowane


if __name__ == "__main__":
    test = asyncio.run(main())
    print(test)