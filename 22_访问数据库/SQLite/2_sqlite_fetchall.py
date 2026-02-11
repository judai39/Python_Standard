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

# 重新认识一下cursor对象，cursor对象又叫做游标对象，和游标卡尺一样，通过在一张表上不断移动，"打点"
# 来记录当前位置（当前位置指的是查询结果中的一行）
# “查询次数不会被覆盖，查询结果会被覆盖”，是因为每次执行查询语句时，游标对象都会更新它的当前位置和
# 查询结果。当我们调用fetchall()方法时，它会返回从当前位置到查询结果末尾的所有行，并将游标对象的当
# 前位置移动到查询结果末尾。因此，如果我们再次执行查询语句，游标对象会更新它的当前位置和查询结果，
# 但之前的查询结果仍然保存在内存中，直到我们调用fetchall()方法来获取它们。

# 为什么需要cursor？如果直接返回查询结果，返回的是一个结果集，但是cursor由于可以迭代，可以对结果集进行处理