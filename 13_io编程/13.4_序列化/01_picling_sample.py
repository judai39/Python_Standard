# 为什么需要序列化？

# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
# d = dict(name='Bob', age=20, score=88)
# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被
# 操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又
# 被初始化为'Bob'。
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

import pickle
import os

diction=dict(name='Bob',age=20,score=88)
# 使用pickle.dump()将数据序列化为bytes，系统再将bytes写入文件完成储存
pickle_obj=pickle.dumps(diction)
# 使用pickle.loads()将bytes文件反序列化
print(pickle.loads(pickle_obj))

# 或者可以使用pickle.dump()将数据写入一个file-like Object
pickle_file=open(os.path.join(os.path.abspath('.'),'dump.txt'),'wb')
pickle.dump(diction,pickle_file)
pickle_file.close()
# 反序列file-like Object对象在02中，使用pickle.load(bytes文件)