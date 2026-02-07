# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 编写模块第一步，先把调用接口写出来
# 例如：想定义一个User类来操作对应的数据库表User，我们期待能够这样写代码：
from b_filed import StringField, IntegerField
from c_model_meta_class import Model
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
user=User(id=12345, name='Michael', email='michael@test.com', password='123456')
user.save() # 保存到数据库
