# 1.正常情况下，未经动态绑定就直接调用一个类没有的属性是会报错的

# 但是由于动态语言的特性，python允许我们动态给一个实例对象绑定属性，如果我们希望固定的返回一个包含
# 一个没有的成员属性的实例对象，我们可以使用__getattr__()方法来实现这个功能 
class Student(object):
    def __init__(self, name):
        self.name = name
    # 没有定义score，但是还是想要返回一个score属性
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # 返回一个函数也是可以的（调用方式从instance.属性-->instance.方法()）
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student('Michael')
print(s.score)
print(s.age())
# 允许返回一个完全没有的属性---->对于一个完全动态的，未知的属性，我们无需重新书写一个单独的方法来获取
# 只需要在__getattr__()方法中返回一个函数或者一个值，就可以满足要求


# 2.正如实例对象动态绑定属性一样，对象实例是可以拥有自己的属性和方法的，那么可以直接在实例对象上调用吗？
# ---->添加定制方法__call__()
class Teacher(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
t = Teacher('Bob')
t() # 直接调用实例对象就可以了