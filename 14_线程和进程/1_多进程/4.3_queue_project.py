# 以写入数据，读取数据为例，展示进程间通信
from multiprocessing import Process,Queue
import os,time,random

# 写入数据进程
def write(q):
    print('Process to write:%s:'%os.getpid())
    for value in ['a','b','c']:
        # 在队列中put数据
        q.put(value)
        print('Put %s to queue...'%value)

# 读取数据进程
def read(q):
    # 防止队列没来得及put数据就被读取
    time.sleep(1)
    print('Process to read:%s:'%os.getpid())
    while True:
        # 将队列中的put数据取出
        value=q.get(True)
        print('Get %s from queue.'%value)

if __name__ == '__main__':
    # 父进程创建Queue，子进程共享队列数据
    q=Queue()
    q='m'
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    # pw进程阻塞主进程，主进程将会等到pw执行完毕才会继续执行
    pw.join()
    pr.join()
    print("所有进程执行完毕")