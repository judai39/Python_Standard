from enum import Enum

# 使用枚举类来定义一个存放批量常量的类型

Month=Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for循环枚举所有类成员
for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)#member.value是自动赋给成员的int常量，默认从1开始计数

# 也可以使用枚举类的成员来获取枚举常量
print(Month.Jan)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import unique
# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

# 访问派生类的属性
print(weekday.Mon)
print(weekday(1))
print(weekday['Mon'])
print(weekday.Mon.value)
