# 因为python为动态语言，所以在运行时才会去检查类型，所以可以在启动时绑定属性和方法
class Student(object):
    pass

if __name__ == '__main__':
    student=Student()
    student.name='Michael'  # 动态给实例绑定一个属性
    print(student.name)

    # 动态绑定一个方法到实例上
    from types import MethodType
    def set_name(self, name):
        self.name = name
    student.set_name=MethodType(set_name,student)  # 动态给实例绑定一个方法
    student.set_name('Tom')
    print(student.name)

    # 但是给另一个实例绑定方法就不行了
    student2=Student()
    # student2.set_name('Jack')  # AttributeError: 'Student' object has no attribute 'set_name'

    # 为了给所有实例都绑定方法，可以给class绑定方法
    def set_age(self, age):
        self.age = age  
    Student.set_age = set_age  # 给class绑定方法
    student.set_age(25)
    print(student.age)
    # 既然可以给class绑定方法，属性，那么我们应该可以对class进行限制，
    # 只允许绑定某些属性，这样就可以节省内存
    # 这就是slots的作用