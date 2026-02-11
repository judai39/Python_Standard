# pip install sqlalchemy
from sqlalchemy import Column, Integer,VARCHAR,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 创建基类对象
Base=declarative_base()
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(VARCHAR(255))
    age=Column(Integer)
    def _str__(self):
        return f'User(id={self.id},name={self.name},age={self.age})'
    def __repr__(self):
        return self._str__()
# 创建数据库连接
engine=create_engine('mysql+mysqlconnector://root:DHY2522609443@localhost:3306/test')
# 创建数据库会话
DBSession=sessionmaker(bind=engine)

# 直接将User实例对象当作数据进行插入
session=DBSession()
new_user=User(name='david',age=20)
session.add(new_user)
session.commit()

# 可以不用fetchall游标查询了
david=session.query(User).filter_by(name='david').first()
print('type:',type(david))
print('name:',david.name)
users=session.query(User).all()#通过命令行传递查询结果，User需要实现__repr__方法，来展示查询结果
print(users)
session.close()
