# 对于一个实例对象的属性，要有一个约束范围才合理
class Student:
    def set_age(self, age):
        if not isinstance(age,int):
            raise ValueError("年龄必须是整数")
        if not (0 <= age <= 120):
            raise ValueError("年龄必须在0到120之间")
        self.set_age=age
    def get_age(self):
        return self.set_age
    # 太麻烦，每次都要写这些代码