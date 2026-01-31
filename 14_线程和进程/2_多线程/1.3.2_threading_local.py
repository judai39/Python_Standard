# 将线程成员交由threading.local()中的成员字典进行管理
import threading

# 1.创建全局TreadLocal()
local_school=threading.local()

class Student:
    def __init__(self,name):
        self.name=name

def process_sutudent():
    # 3.local_school.studetn_dict分发student()对象
    student=local_school.student_dict
    print('hello,%s (in %s)'%(student.name,threading.current_thread().name))

def process_thread(name):
    # 2.存储到ThreadLocal的student_dict对象
    local_school.student_dict=Student(name)
    process_sutudent()

t1=threading.Thread(target=process_thread,args=('小明',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('小刚',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()