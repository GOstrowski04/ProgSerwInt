import asyncio


async def main(n) -> None:
    l1 = 0
    l2 = 1
    while n >= 0:
        n -= 1
        await asyncio.sleep(1)
        print(l1)
        l1 += l2
        await asyncio.sleep(1)
        print(l2)
        n -= 1
        l2 += l1


if __name__ == '__main__':
    asyncio.run(main(5))