import asyncio

async def print1():
    print(1)
    
async def print2():
    await asyncio.sleep(2)
    print(2)

async def print3():
    print(3)

async def main():
    tsk1 = asyncio.create_task(print1())
    tsk2 = asyncio.create_task(print2())
    tsk3 = asyncio.create_task(print3())

    # await tsk1
    # await tsk2
    # await tsk3
    await asyncio.gather(tsk1, tsk2, tsk3)

asyncio.run(main())