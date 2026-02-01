import time,sys,queue
from multiprocessing.managers import BaseManager

# ----任务端代码---- #

class QueueManager(BaseManager):
    pass

# 注册获取Queue的方法名称（与服务端master保持一致）
# task_master已经把队列名暴露到网络中了
# 任务端task_worker仅需提供名称即可
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器（连接task_master）
server_address='127.0.0.1'
manager=QueueManager(address=(server_address,5000),authkey=b'dhy')

# 连接到网络服务器
manager.connect()

# 从网络上获取Queue对象，并进行本地化，与服务进程是同一个队列
task=manager.get_task_queue()
result=manager.get_result_queue()

# 从服务端获取数据，并把结果写入到result队列中
for i in range(10):
    n=task.get(timeout=1)
    print("run task %d * %d..."%(n,n))
    time.sleep(1)
    result.put(n*n)
print("worker exit...")