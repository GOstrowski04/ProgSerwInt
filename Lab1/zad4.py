import asyncio

async def main() -> None:
    for x in range(1, 6):
        await asyncio.sleep(1)
        print(x)


if __name__ == '__main__':
    asyncio.run(main())