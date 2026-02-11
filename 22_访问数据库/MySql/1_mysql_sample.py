# pip install msyql-connector-python
import mysql.connector

# 创建数据库（cmd运行）
# CREATE DATABASE test CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

connection=mysql.connector.connect(user='root',password='DHY2522609443',database='test')
cursor=connection.cursor()
# 创建user表
cursor.execute("CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INTEGER)")
# 插入数据（注意MYSQL占位符是%）
cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",('alice',20))
cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",('bob',22))
connection.commit()

# 更新
cursor.execute("UPDATE user SET age=%s WHERE name=%s",(90,'alice'))
connection.commit()

# 查询
cursor.execute("SELECT * FROM user")
for user in cursor.fetchall():
    print(user)

cursor.close()
connection.close()