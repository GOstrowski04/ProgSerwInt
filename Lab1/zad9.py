import asyncio

async def maszynaA() -> None:
    while True:
        await asyncio.sleep(2)
        print("Cykl maszyny A wykonany.")

async def maszynaB() -> None:
    while True:
        await asyncio.sleep(3)
        print("Cykl maszyny B wykonany.")

async def maszynaC() -> None:
    while True:
        await asyncio.sleep(5)
        print("Cykl maszyny C wykonany.")


async def main() -> None:
    try:
        async with asyncio.timeout(16):
            await asyncio.gather(maszynaA(), maszynaB(), maszynaC())
    except asyncio.TimeoutError:
        print("Zakończono pracę po 15 sekundach")

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())