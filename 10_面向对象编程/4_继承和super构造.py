# 引入:在一个继承结构中,子类调用父类的构造器方法会非常麻烦,因为父类的名字可能会发生变化,
# 而且在多重继承中,父类的名字更是难以确定.为了解决这个问题,Python提供了一个super()函数来调用父类的方法.

# 1.不使用super()函数的多重继承
class Animal(object):
    def __init__(self, name):
        self.name = name
        print("i'm an animal")

class Dog1(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print("i'm a dog1")

class Dog2(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print("i'm a dog2")

class DogSon(Dog1,Dog2):
    def __init__(self, name):
        Dog1.__init__(self, name)
        Dog2.__init__(self, name)
        print("i'm a dogson")
DogSon("gou")   #实例化多重继承,依次调用了Dog1,Dog2两个的父类构造器方法,我们只希望父类构造器被调用一次

# 2.super()函数的使用
class Cat1(Animal):
    def __init__(self, name):
        super(Cat1, self).__init__(name)
        print("i'm a cat1")
class Cat2(Animal):
    def __init__(self, name):
        super(Cat2, self).__init__(name)
        print("i'm a cat2")
class CatSon(Cat1,Cat2):
    def __init__(self, name):
        super(CatSon, self).__init__(name)
        print("i'm a catson")
CatSon("mao")   #Animal构造器没有被重复调用

# 3.super()底层原理
# 我们知道,python的动态性质其实是由于python中的类是类似于spring框架中的aop结构,即"类的实例已经存在,我们只负责组装"
# 那么组装的具体是什么呢?是基于type的一个元类对象,我们在创建一个类的时候,python会自动调用type.__new__()方法来创建一个类的实例对象
# 而super()函数就是在这个过程中被组装到类中的一个方法,当我们调用super()函数时,实际上是调用了这个方法,它会根据当前类的继承关系来确定应该调用哪个父类的方法.
# ....
# 以上知识,我们还是不理解,super是怎么匹配到父类的...
# 我们可以通过查看类的mro方法来了解类的继承关系,从而理解super()函数的工作原理.
# def super(cls, inst):
#   mro = inst.__class__.mro()
#   return mro[mro.index(cls) + 1]
# 通过上面的代码,我们可以看到,super()函数实际上是通过类的mro方法来获取类的继承关系,然后根据当前类的位置来确定应该调用哪个父类的方法.
# cls是为了告诉系统,我们现在处于哪个类中,inst是为了告诉系统,我们现在操作的是哪个实例对象.
# 这样系统就知道了当前实例对象的下一个cls的index位置(mro()返回一个继承关系列表)
print(CatSon.mro())#查看CatSon中的mro()方法返回的继承关系列表

# 4.顺便看看其他关键的类属性吧
print(CatSon.__class__)   #查看CatSon的类属性,返回<class 'type'>,说明CatSon是一个类对象
print(CatSon.__bases__)   #查看CatSon的基类属性,返回(<class '__main__.Cat1'>, <class '__main__.Cat2'>),说明CatSon继承了Cat1和Cat2两个类
print(CatSon.__dict__)    #查看CatSon的字典属性,返回一个字典对象,包含了CatSon类的所有属性和方法,包括从父类继承来的属性和方法    
CatSon._attrs_="animal_attrs"
