# 如协程sample所示，协程代码是一个有yield控制的while true循环，python把这样的一个循环抽离出来，成为asyncio消息循环
import asyncio
import threading
async def hello(name):
    print("Hello:%s（%s）"%(name,threading.current_thread))
    # 异步调用并发的asyncio.sleep(1)
    await asyncio.sleep(1)
    # 并发操作，在同一个线程中
    print("Hello again:%s（%s）"%(name,threading.current_thread))

async def main():
    # 使用asyncio.gather()同时调度多个异步操作
    await asyncio.gather(hello("Bob"),hello("alice"))

asyncio.run(main())