from io import StringIO

# 许多时候，写入操作不一定发生在文件中，也可能发生在内存中

# 1.StringIo
# StringIo写入内存
file=StringIO()
file.write('hello')
file.write('_')
file.write('world')
print(file.getvalue())
# String读取内存
file=StringIO('hello\nHi\nGoodbye')#将字符流当作文件存储到内存中
while True:
    str=file.readline()
    if str=='':#''不是空值，不能使用None判断
        break
    print(str.strip())

# 2.BytesIo
from io import BytesIO
# Bytes写入内存
file=BytesIO()
file.write('字符串'.encode('utf8'))
print(file.getvalue())
# Bytes读取内存
file=BytesIO(b'\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2')
print(file.read())