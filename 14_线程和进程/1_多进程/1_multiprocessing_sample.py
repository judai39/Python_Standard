from multiprocessing import Process
import os
import time

# 待执行的代码
def to_run_processing1(name):
    time.sleep(5)
    print('Run child 进程1 %s (%s)...'%(name,os.getpid()))
def to_run_processing2(name):
    time.sleep(10)
    print('Run child 进程2 %s (%s)...'%(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s...'%os.getpid())
    # 创建子进程
    p1=Process(target=to_run_processing1,args=('processing1',))
    p2=Process(target=to_run_processing2,args=('processing2',))
    print('Child process will start...')
    # 启动子进程
    p1.start()
    p2.start()
    # 尝试一下将p1,p2分别加入主进程，看看处理顺序会有什么不同
    p1.join()#p1
    # p2.join()
    print('Child process end...')

# 可以发现，如果一个进程被添加到主进程，那么主进程就会被堵塞【在本例中的体现就是
# print('Chile process end...)代码会一直等到堵塞主进程的那个子进程运行结束才会结束】