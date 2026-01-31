# 很多时候，子进程不会是主进程自身，而是外部的程序
import subprocess

# 使用subprocess模块自带的call()直接调用命令行（像不像batch命令中的call [path]）
r=subprocess.call(['nslookup','www.python.org'])#等同于cmd+nslookup www.python.org
print('Exit code:',r)

# 如果子进程还需要输入，则还可以通过communicate()方法输入
# subprocess.Popen()打开一个命令行，输入命令以创建新进程
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\next\n')
print(output.decode('utf-8'))
print('Exit Code:',p.returncode)

#Popen()进程参数：
# args：要执行的命令，可以是字符串或程序参数的序列。
# stdin、stdout、stderr：分别指定子进程的标准输入、输出和错误管道（out,err可以被捕获）。
# shell：如果为 True，则通过系统的 shell 执行指定命令。
# cwd：设置子进程的当前工作目录。
# env：定义新进程的环境变量。 

# ^ # ^：stdout 和 stderr 被重定向到管道，这意味着你可以从 Python 中捕获和处理这些输出。