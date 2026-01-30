# 和04_multiprocessing_queue.py对比，如果没有进程通信，如何让两个子进程交换数据
# 不同进程之间肯定是需要通信的（数据交换），pyton的multiprocessing模块中提供Queue，Pipe等方式实现
from multiprocessing import Process,Queue
import os,time,random

num=100

# 写入数据进程
def write():
    global num
    print('Process to write:%s:'%os.getpid())
    num+=50
    print('Put %s to queue...'%num)
    time.sleep(random.random()*5)

# 读取数据进程
def read():
    global num
    print('Process to read:%s:'%os.getpid())
    num-=50
    print('Get %s from queue.'%num)

if __name__ == '__main__':
    print("全局变量num开始时为：",num)
    pw=Process(target=write,args=())
    pr=Process(target=read,args=())
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print("全局变量num结束时为：",num)

# 运行结果为：一直输出的q值为num
#   为什么在pw进程覆盖了q值后，pr进程打印的依然是覆盖前的值？
# ----因为传入参数的args是初始的值，进程在运行前接受的值都是'num'，
#     两个进程是两个独立的实例对象，无法交换数据
# -->进程通信的必要性
# -->大胆假设：实现进程通信需要什么？
#             -->Process()上层类对不同的Process有共享域

