# 在多线程中：
# 线程中的局部变量不受影响，全局变量可能会被错误更改，需要上锁
# 如果我要传递一个线程对象（Student()），该怎么办？
    # （1）Student()设为全局变量？  --不行，每个线程处理的Student应该是不同的
    # （2）如果用一个全局dict存放所有的Student对象，然后以thread线程码自身作为key获得
import threading,time
class Student:
    def __init__(self,name):
        self.name=name

global_dict={}

def std_thread(name):
    student=Student(name)
    # threading.current_thread()将会返回当前的线程名作为对应当前学生的key
    global_dict[threading.current_thread()]=student
    do_task1()
    do_task2()

def do_task1():
    student=global_dict[threading.current_thread()]
    print(f"{student.name}在做任务1")
    time.sleep(1)
def do_task2():
    student=global_dict[threading.current_thread()]
    print(f"{student.name}在做任务2")
    time.sleep(1)

if __name__ == '__main__':
    std_thread("小明")
    std_thread("小红")
    std_thread("小刚")
# 有点麻烦了，有没有更简单的方法？
    # （3）ThreadLocal