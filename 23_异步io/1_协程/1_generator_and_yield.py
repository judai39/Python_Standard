# yield相当于可以冻结当前线程的return,返回由yield后面的状态值决定
# 同时,在调用send(value)后,yield前的变量会被value赋值
# next()会让生成器前进，next()会前进到yield所在位置（注意：没有next，生成器是不会自动执行的，哪怕已经调用）
def coroutine_example():
    value=yield 0
    print(f"第一次value:{value}")
    value=yield
    print(f"第二次value:{value}")
    value=yield 1
    print(f"第三次value:{value}")
    value=yield student
    print(f"生成器生成student，我是{student}")

class student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name

c=coroutine_example()
print(next(c))
print(next(c))
print(next(c))
print(c.send(student("小明")))#如果需要传入一个实例对象，肯定是要"动态"的传入，不可能直接在生成器里yield后生命
