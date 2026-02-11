# 为什么需要生成器？
# 如果我们需要获取一个包含一个亿元素的列表，我们需要先创建这个列表，在添加元素
# 但是添加元素是从1开始的，在从1开始之前，我们却创建了一个一个亿大小的空列表，太浪费了
# ---->需要一个生成器，动态的分配内存，动态的生成元素


# 1.把列表生成式的[]换成()就变成了生成器表达式
g=(x for x in range(1,11))#生成器储存的是算法
next(g)
next(g)#...

# 2.函数内添加yield关键字，就可以视为生成器
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b#每次调用next()时，函数执行到yield语句就返回yield后面的值，并冻结当前状态
               # (和return很像，但return是退出函数，而yield是暂停函数)
        a,b=b,a+b
        n+=1
    return 'done'
f=fib(10)
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print('Generator return value:',e.value)
        break