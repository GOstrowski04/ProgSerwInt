import asyncio

async def main(n) -> None:
    a1 = 0
    a2 = 1
    while n > 0:
        await asyncio.sleep(1)
        print(a1)
        temp = a1
        a1 = a2
        a2 = temp + a2
        n -= 1
if __name__ == "__main__":
    asyncio.run(main(10))