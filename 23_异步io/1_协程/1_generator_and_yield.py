# yield相当于可以冻结当前线程的return,返回有yield后面的状态值决定
# 同时,在调用send(value)后,yield前的变量会被value赋值(如果没有进行赋值,关于yield前变量有关的操作不会被执行)
# next()会让生成器前进
def coroutine_example():
    value=yield 0
    print(f"Receicved value:{value}")
    value=yield 1
    print(f"Received value:{value}")

c=coroutine_example()
print(next(c))
print(c.send(2))