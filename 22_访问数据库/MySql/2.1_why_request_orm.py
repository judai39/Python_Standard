import mysql.connector

connection=mysql.connector.connect(user='root',password='DHY2522609443',database='test')
cursor=connection.cursor()
cursor.execute("SELECT * FROM user")
# 以test数据库为例，查询user表中的数据，user(id(Int),name(Varchar),age(Int))
# 查询结果是一个元组列表，每个元组代表一行数据
for user in cursor.fetchall():
    print(user)
# 可以把关系数据库的表结构映射到对象中，从而实现数据库和python的交互----通过orm框架来实现
cursor.close()
connection.close()