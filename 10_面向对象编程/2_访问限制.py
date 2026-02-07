# 我们希望对不同的类有不同的访问权限

# 1.__param 私有属性
# 在Python中，以双下划线开头的属性或方法是私有的，外部无法直接访问
class Student:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age    # 私有属性

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")
# 双下滑线的属性__name在metaclass中被解释为_Student__name，可以通过Student._Student__name访问，但不建议这样做，因为它破坏了封装性
print(Student("david",30)._Student__name)

# 2._param 保护属性
# 在Python中，以单下划线开头的属性或方法是保护的，外部可以访问但应避免直接修改
class Teacher:
    def __init__(self, name, subject):
        self._name = name   # 保护属性，外部可以访问但应避免直接修改
        self._subject = subject  # 保护属性

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
Teacher._name = "New Name"  # 虽然可以访问和修改，但不建议这样做

