# 变量在主进程中：所有子进程都拥有该变量的一个复制文件
# 变量在主线程中：所有子线程都可以操作该变量的数据，容易把变量改乱了
import time,threading

bank_balance=0

def change_it(num):
    global bank_balance
    bank_balance+=num
    time.sleep(1)
    bank_balance-=num


def run_thread(num):
    for i in range(100000000):
        change_it(num)
        print(bank_balance)
        # time.sleep(1)


thread1=threading.Thread(target=run_thread,args=(5,))
thread2=threading.Thread(target=run_thread,args=(8,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(bank_balance)
# 两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成
# 了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。