import sqlite3
import os

# 为什么fecthall不需要我们额外赋值一个存储对象？难道说它会自己创建一个对象来存储查询结果吗？是的，fetchall()会返回一个包含所有查询结果的列表对象，我们可以直接使用这个列表对象来访问查询结果，而不需要我们自己创建一个存储对象来存储查询结果。
db_file=os.path.join(os.path.abspath("."),"test.db")
connection=sqlite3.connect(db_file)
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR(20), age INTEGER)")
cursor.execute("INSERT INTO users (name,age) VALUES ('bob',25)")
cursor.execute("INSERT INTO users (name,age) VALUES ('alice',30)")
connection.commit() 
# 将下面两个查询反复交替执行
# cursor.execute("SELECT NAME FROM USERS WHERE AGE=25")
cursor.execute("SELECT NAME FROM USERS WHERE AGE=30")

# 会发现，fetchall返回了一个列表，里面的查询次数会被保留，重复执行了多少次，就会返回多少个列表，至于每
# 个列表中的查询结果是怎样，根据当前的查询语句而定（如果两个都没被注释，每个列表中的数据都是最后一个查询结果）
# 结论：查询次数不会被覆盖，查询结果会被覆盖
for user_name in cursor.fetchall():
    print(user_name)
connection.close()
