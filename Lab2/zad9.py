import aiohttp
import asyncio

async def fetch(url: str) -> str:
    attempt = 0
    maxAttempts = 3
    async with aiohttp.ClientSession() as session:
        while attempt < maxAttempts:
            async with session.get(url) as response:
                if 200 <= response.status < 300:
                    return await response.json()
                elif 500 <= response.status < 600:
                    attempt += 1
                    print("Błąd serwera, liczba prób: {attempt}")
                else:
                    return None
    print("Maksymalna liczba prób osiągnięta.")
    return None

async def main() -> str:
    url = "https://68e6851b21dd31f22cc5ffad.mockapi.io/api/v1/user"
    tasks = [fetch(url) for i in range(100)]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    asyncio.run(main())