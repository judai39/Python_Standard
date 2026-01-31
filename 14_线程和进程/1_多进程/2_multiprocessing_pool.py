# 如果要启动大量子进程，使用进程池的方式批量创建子进程
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run Task %s(%s)'%(name,os.getpid()))
    # 我运行一个非延时性程序，并没有分配到不同的进程执行
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f second.'%(name,(end-start)))


if __name__ == '__main__':
    print('parent process %s'%os.getpid())
    p=Pool()#默认为4
    for i in range(5):
        # 系统向池子发送子进程操作逻辑,已经排列好了所有进程的执行逻辑和顺序,只欠调用!
        p.apply_async(long_time_task,args=(i,))
    print('Waitting for all subprocessing done...')
    # 这之后要封装池子,方便后续通过实例化池子对象,并将池子送到系统进程上
    p.close()
    # 送到系统进程上
    p.join()
    print('All subprocessing done...')
    # 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后
    # 才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool
    # 有意设计的限制，并不是操作系统的限制。如果改成：

    # 关于Pool()池子实例的默认进程数量--默认为4，因为我的电脑是4核处理