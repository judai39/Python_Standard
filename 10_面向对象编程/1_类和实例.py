# 和java不同，python中的类底层是维护着一个type类型的实例的（metaclass），是动态的
# 0.那么，什么是动态呢？

# 持续化动态（也可以叫动态包装），和spring框架中的aop类似（aop切面分割出的多个部分都会被单独存放，最终通过代理方法组装），
# python中的类也是动态创建的，python解释器在执行到class语句时，会调用type()函数来创建一个类对象，这个类对象就是type
# 类型的实例。
class Person:
    @classmethod
    def get_person(cls):
        return cls.__name__
    pass
print(type(Person))#<class 'type'>，Person是type类型的实例
print(type(int))#<class 'type'>，int是type类型的实例(java中的int是基本类型，不是对象，所以没有type类型的实例,是包装类Integer的实例)

# 1.由于是动态创建类实例，因此可以在运行时动态修改类的属性和方法：
def set_age(self,age):
    self.age=age
person=Person()
person.set_age=set_age#为单个person实例对象添加实例对象方法
Person.set_name=lambda self,name: setattr(self,'name',name)#为Person类添加类方法

# 2.什么叫类方法，实例方法？
# 实例方法：定义在类中的函数，第一个参数是self，表示实例本身（仅当前实例可以调用）
# 类方法：我们希望,将实例化对象中的批量的相同属性和方法抽取出来,放在类中,通过@classmethod装饰器定义（所有实例都可调用）
class student:
    teacher="小白"#本班中的所有学生的老师都是小白,所以这个属性应该是属于类的是类属性,因此可以放在类里

    @classmethod#类方法
    def get_teacher(cls):
        return cls.teacher#返回的是类属性teacher,即使实例化后修改teacher属性,也不会影响类属性teacher的值
s1=student()
s1.teacher="小黑"
print(s1.get_teacher())#小白
print(student.get_teacher())#也可以通过类名调用

# 3.什么是静态方法？
# 静态方法：定义在类中的函数，没有默认参数（既不是self也不是cls），通过@staticmethod装饰器定义（所有实例都可调用）
class static_person:
    @staticmethod
    def get_person():
        return 'static_person'
# 静态方法也可以通过类名调用
print(static_person.get_person())
# 静态方法和类方法的区别：
# 类方法可以访问和修改类状态（通过cls），实例方法可以访问和修改实例状态（通过self）
# 静态方法不能访问或修改类状态（没有cls也没有self），它们只是一个普通函数，放在类的命名空间中。
