class Student:
    # getter方法用于获取属性值
    @property
    def age(self):
        return self._age

    # setter方法用于设置属性值
    @age.setter
    def age(self, value):
        if not (0 <= value <= 120):
            raise ValueError("年龄必须在0到120之间")
        self._age = value

if __name__ == '__main__':
    student=Student()
    student.age=130
    print(student.age)