import random,time,queue
from multiprocessing.managers import BaseManager
# ----服务端代码---- #


# 发送任务的队列：
task_queue=queue.Queue()
# 接收任务的队列：
result_queue=queue.Queue()

# 返回队列的函数（用以序列化，因为lambda方法在windows平台无法序列化）
def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue

# 创建QueueManager(继承自BaseManager)，交由QueueMnanager管理不同机器间的进程通信
class QueueManager(BaseManager):
    pass

# 不同于linux系统中fork()封装到多进程类中，主进程创建子进程通过fork()直接复制过去，子进程
# 只需要通过get()相关方法即可获取到主进程，windows系统中没有fork()方法，因此创建子进程
# 实现多任务效果需由系统手动分配，这也就要求了在调用相关创建子进程的方法时一定要声明在main()中
if __name__ == '__main__':
    # 将两个Queue都注册到网络上，callable参数关联Queue对象：
    QueueManager.register('get_task_queue',callable=return_task_queue)
    QueueManager.register('get_result_queue',callable=return_result_queue)
    # 绑定端口为5000，设置验证码为‘dhy’:
    manager=QueueManager(address=('127.0.0.1',5000),authkey=b'dhy')
    # 启动Queue：
    manager.start()
    # 获得通过网络访问的Queue对象：
    task=manager.get_task_queue()
    result=manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n=random.randint(0,10000)
        print('put task %d ...'%n)
        task.put(n)
    # 从result队列读取结果：
    print('Try get results...')
    for i in range(10):
        r=result.get(timeout=10)
        # --执行完任务端代码后输出继续输出print
        print('Result:%s'%r)
    # 关闭:
    manager.shutdown()
    print('master exit...')

# 运行单个文件总是报错，报错为队列is empty，也就是result的队列为空，因为接下来我们要在另一个文件中
# 用到该进程的task数据，进而实现分布式进程