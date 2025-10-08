import asyncio


async def fetch(delay: int) -> int:
    await asyncio.sleep(delay)
    print(10)
    return 10
async def main():
    await asyncio.gather(fetch(3), fetch(10), fetch(6), fetch(7), fetch(2))

if __name__ == "__main__":
    asyncio.run(main())