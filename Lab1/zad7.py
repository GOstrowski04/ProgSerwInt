import asyncio


async def krojenie(czas: int) -> None:
    await asyncio.sleep(czas)
    print("Pokrojono.")

async def gotowanie(czas: int) -> None:
    await asyncio.sleep(czas)
    print("Ugotowano.")

async def smazenie(czas: int) -> None:
    await asyncio.sleep(czas)
    print("Usmażono.")

async def danie(n1: int, n2: int, n3: int) -> None:
    await asyncio.gather(krojenie(n1), gotowanie(n2), smazenie(n3))
    print("Danie ukończone.")

async def main() -> None:
    await asyncio.gather(danie(2, 5, 3), danie(4, 2, 3), danie(1, 3, 1))

if __name__ == "__main__":
    asyncio.run(main())