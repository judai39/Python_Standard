# 如果一个类想被用于for...in循环中，就必须实现一个__iter__()方法，该方法返回一个迭代器对象
# 迭代器对象必须实现一个__next__()方法，该方法在每次调用时返回容器的下一个元素
# 迭代器可以实现__getitem__()方法，可以按索引顺序访问元素，但不推荐这样做
class fib(object):
    def __init__(self):
        self.n, self.a, self.b = 0, 0, 1

    # 实例本身就是迭代对象，故返回自己
    def __iter__(self):
        return self

    # for循环会自动调用__next__()方法获取下一个元素
    def __next__(self):
        if self.n < 20:
            r = self.a
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
    
    # 实现__getitem__方法，使得该类也可以按索引访问元素
    def __getitem__(self, n):
        a, b = 0, 1
        for x in range(n):
            a, b = b, a + b
        return a

for n in fib():
    print(n)
print(fib()[7])  # 输出第5个斐波那契数