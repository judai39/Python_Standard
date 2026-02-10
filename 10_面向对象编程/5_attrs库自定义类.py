# pip install attrs
import attrs

# 为什么需要attrs?
# python类由于没有构造函数的参数类型检查，所以在创建对象时很容易出错，attrs库提供了一种简洁的方式来定义类，
# 并且可以自动生成构造函数、比较方法等，同时还支持类型检查和默认值设置。

# 1.attrs定义类属性
@attrs.define
class Person:
    name: str=attrs.field(default="张三")
    age:int=attrs.field(default=18)
    # 将自动生成__init__,__repr__,__eq__等方法

p1=Person("ddd",30)
print(p1) 

# 2.attrs检查类属性合法性
def check_postive(instance, attribute, value):
    if value < 0:
        raise ValueError(f"{attribute.name} must be positive")
@attrs.define
class product:
    name:str
    price:float=attrs.field(validator=check_postive)
try:
    print(product("电脑",-5000))
except ValueError as e:
    print(e)

# 3.attrs实例对象序列化
@attrs.define
class Student:
    name: str
    age: int
    score: float
# 序列化为字典
student = Student("张三", 20, 85.5)
print(attrs.asdict(student))

# 4.attrs.defined装饰器的参数
# 4.1 slots=True: 使用__slots__来优化内存使用，禁止动态添加属性
@attrs.define(slots=True)
class Point:
    x: int
    y: int
p=Point(1,2)
print(p)
# 4.2 frozen=True: 使实例不可变，禁止修改属性值
@attrs.define(frozen=True)
class ImmutablePoint:
    x: int
    y: int
ip=ImmutablePoint(3,4)
# ip=ImmutablePoint(5,6) 
# 4.3 auto_attribs=True: 自动推断属性类型，无需显式声明类型
@attrs.define(auto_attribs=True)
class AutoPoint:
    x="默认值"
    y=0
ap=AutoPoint()
print(ap.x,ap.y)