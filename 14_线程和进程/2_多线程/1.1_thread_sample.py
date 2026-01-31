import time,threading

# 新线程执行的代码
def loop():
    print('thread %s is running ...'%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.'%threading.current_thread().name)

if __name__ == '__main__':
    print('thread %s is running...'%threading.current_thread().name)
    thread=threading.Thread(target=loop,name='LoopThread')
    thread.start()
    thread.join()
    print('thread %s is ended.'%threading.current_thread().name)