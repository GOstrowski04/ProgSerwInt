import asyncio


async def kr1() -> None:
    await asyncio.sleep(3)
    print("Korutyna 1")


async def kr2() -> None:
    await asyncio.sleep(1)
    print("Korutyna 2")


async def main() -> None:
    task1 = asyncio.create_task(kr1())
    task2 = asyncio.create_task(kr2())
    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())
