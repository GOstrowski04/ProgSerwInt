import asyncio

async def wczytanie() -> None:
    await asyncio.sleep(2)
    print("Wczytano plik.")

async def analiza() -> None:
    await asyncio.sleep(4)
    print("Zanalizowano plik.")

async def zapis() -> None:
    await asyncio.sleep(1)
    print("Zapisano plik.")

async def przetwarzanie() -> None:
    await asyncio.gather(wczytanie(), analiza(), zapis())

async def main() -> None:
    await asyncio.gather(przetwarzanie(), przetwarzanie(), przetwarzanie(), przetwarzanie(), przetwarzanie())

if __name__ == "__main__":
    asyncio.run(main())