# 如果我们直接输出一个实例对象，将会输出该实例对象的内存地址（<__main__ object at 0x...>）
# 我们可以让该类继承自 object 类，并重写 __str__ 方法，从而实现自定义的字符串输出
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

p = Person('Alice', 30)
print(p)  # 输出: Person(name=Alice, age=30)

# 但是，如果我们在命令行输出该实例对象（不使用print）
# 会输出该对象的内存地址，而不是我们自定义的字符串表示
# 这是因为 __str__ 方法只在使用 print() 时被调用
# 而在命令行中直接输出对象时，Python 会调用 __repr__ 方法
# 所以我们还需要重写 __repr__ 方法来实现更完整的自定义输出
class PersonWithRepr(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __repr__(self):
        return f'PersonWithRepr(name={self.name}, age={self.age})'
p_repr = PersonWithRepr('Bob', 25)
# 在命令行直接输出p_repr