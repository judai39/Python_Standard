# python操作电脑系统中的对象----调用操作系统提供的接口函数os
import os

print(os.name)#输出系统信息
# print(os.uname()) 输出详细的系统信息（windows系统不适用）
print(os.environ)#输出环境变量
print(os.environ.get('path'))#输出环境变量中的对应字段

# 1.操作文件目录
# （1）查看当前目录的绝对路径
os.path.abspath(".") 
# （2）在根目录下创建一test_dir目录(join创建)
test_dir=os.path.join(r'C:/Users/User/Desktop\Python_Standard','test_dir')
os.mkdir(test_dir)
# （3）删除目录
os.rmdir(test_dir)
# 上面的路径可以看到，在输入目录\或/都可以读取，但是输出的信息不通，windows输出\，linux，mac等输出/
# 为了适配性，尽可能不要拼写路径
windows_mkdir1=os.path.join(r'C:/Users/User/Desktop\Python_Standard','test_dir')#合并路径
windows_mkdir2=os.path.split('C:/Users/User/Desktop/Python_Standard')#分开路径
print(windows_mkdir1,"\n",windows_mkdir2)
# 顺带一提，splitext可以分离文件后缀
print(os.path.splitext("/path/to/file.txt"))#以“.”为目标分离字符串

# 2.操作文件
# （1）新建文件
file_path=os.path.join(os.path.abspath("."),"test.txt")
with open (file_path,'w')as file:
    file.write("")
# （2）文件重命名
os.rename('test.txt','test.py')
# （3）删除文件
os.remove('test.py')
# （4）复制，移动文件（os库本身没有，需要引入shutil模块中的copyfile()）

# 使用python高级特性-生成器过滤文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 使用python高级特性-生成器过滤md文件
print([x for x in os.listdir('.')if os.path.isfile(x) and os.path.splitext(x)[1]=='.md'])