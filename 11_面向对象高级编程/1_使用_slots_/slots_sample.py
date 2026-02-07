# 使用slots限制实例的属性
class Person:
    __slots__ = ('name', 'age')  # 只允许这两个属性
class Student(Person):
    __slots__ = ('name','age')  # 只允许这一个属性

if __name__ == '__main__':
    person=Person()
    person.name='michael'
    person.age=23
    # person.score=90 # 会报错，AttributeError: 'Person' object has no attribute 'score'

    # __属性会被继承，子类也只能定义__slots__属性中定义的属性
    student=Student()
    student.name='michael'
    student.age=23