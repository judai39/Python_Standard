import asyncio

# 任务协程可以通过asyncio.create_task()直接调用

async def hello():
    await asyncio.sleep(1)
    print("hello")
async def world():
    await asyncio.create_task(hello())
    await asyncio.sleep(1)
    print("world")

asyncio.run(world())