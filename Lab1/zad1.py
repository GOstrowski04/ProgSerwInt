import asyncio


async def main() -> None:
    await asyncio.sleep(2)
    print("Oczekiwanie zakończone")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())
