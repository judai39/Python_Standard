
try:
    file=open(r'C:\Users\User\Desktop\emi.txt','r')
except IOError:
    print("文件读写异常")
else:
    print(file.read())
    file.close()

# 这样写太繁琐了-->简化为with,as语句(这将会自动调用close（）语句)
with open(r'C:\Users\User\Desktop\emi.txt','r') as file:
    print(file.read())

# 关于read()
# read()会把文件全部读取,在读取大文件时会卡死,因此可以尝试使用:
file=open(r'C:\Users\User\Desktop\emi.txt','r')
for line in file.readlines():#readlines()只会读取一行
    print(line.strip())
# 或者
print(file.read(1024))#约束大小
file.close()