# 动态语言和静态语言最大的不同，就是函数和类的定义，在动态语言中，函数和类的定义是运行时执行的，
# 而在静态语言中，函数和类的定义是在编译时执行的。
# 以命令行模式运行代码举例，java要先使用命令javac成字节码，然后再使用命令java运行，
# 但是python允许我们一行一行输入代码，执行一半继续输入代码等等操作，这统称为动态语言的交互式编程。
# 例如:
class Hello(object):
    def hello(self,name='world'):
        print('Hello, %s.' % name)
# 在命令行执行下应该是这样：
# >>> from hello import Hello
# >>> h = Hello()
# >>> h.hello()
# Hello, world.
# >>> print(type(Hello))
# <class 'type'>
# >>> print(type(h))
# <class 'hello.Hello'>

# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就
# 是class Hello。

# 我们说class的定义是运行时执行的，实际上就是在运行时动态创建了一个class对象，Hello是这个class对象的名字，
# type()函数既可以返回一个对象的类型，又可以创建出一个新的类型，例如:
def fn(self,name='world'):
    print('Hello, %s.' % name)
Hello = type('Hello',(object,),dict(hello=fn))
# 上面代码创建了一个Hello class，类型就是type，函数fn被绑定到
h=Hello()
h.hello()
print(type(Hello))
print(type(h))