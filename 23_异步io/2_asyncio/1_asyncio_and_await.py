# asyncio是 Python 中用于编写异步代码的标准库，它提供了一组工具和API来管理和调度协程。通过asyncio，可以轻松创建、执行和
# 管理异步任务。
# 是异步并发的
import asyncio

# async关键字用于定义异步函数
async def asyncio_function():
    # await关键字用于暂停异步函数的执行，等待另一个异步任务完成。
    await asyncio.sleep(1)
    print("asyncio function executed")


# asyncio.run(asyncio_function())   直接run运行协程

# gather调度群体协程(本质就是用gather包装嵌套了其他的协程方法进行执行)
async def main():
    await asyncio.gather(asyncio_function(),asyncio_function())
asyncio.run(main())