# SQLite是一种嵌入式数据库，因为体积小，使用方便，适合在小型项目中使用。
# Python内置了sqlite3模块，可以直接使用SQLite数据库。

# 表：表是数据库中存放“关系数据”的结构化集合

import sqlite3

# 1.创建连接对象
connection=sqlite3.connect("test.db")
# 2.创建游标对象
cursor=connection.cursor()
# 3.执行SQL语句
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR(20), age INTEGER)")
cursor.execute("INSERT INTO users (name,age) VALUES ('Alice', 30)")
print("插入的行数为：%s"%cursor.rowcount)
# 4.提交事务
connection.commit()
# 5.关闭连接
connection.close()

# 这样就生成了名为test.db的sqlite数据库文件

# 试着查询
conn=sqlite3.connect("test.db")#如果再次声明为connection,python系统会进行优化，认为它是同一个对象，所以我们改为conn
cursor=conn.cursor()
cursor.execute("SELECT * FROM users")
# 使用fetchall()获取所有查询结果（fetchall()会返回cursor执行的所有SELECT结果）
for row in cursor.fetchall():
    print(row)
conn.close()