import threading,time

bank_balance=0
# 0.实例化lock()对象
lock=threading.Lock()

def change_it(num):
    global bank_balance
    bank_balance+=num
    time.sleep(1)
    bank_balance-=num

def run_thread(num):
    for i in range(100000000):
        # 对数值修改函数上锁
        # 1.获取实例化后的lock()对象
        lock.acquire()
        # 2.try代码块上锁代码
        try:
            change_it(num)
        finally:
            # 3.调用完毕，释放locK()实例对象
            lock.release()
        print(bank_balance)


thread1=threading.Thread(target=run_thread,args=(5,))
thread2=threading.Thread(target=run_thread,args=(8,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(bank_balance)
# 缺点：本来一颗cpu可以执行多个线程，但是由于上锁，导致只能依次执行一个进程，大大降低效率