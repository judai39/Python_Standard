# 在动态语言中，不同于java这种静态语言，需要通过编译来判断代码是否正确，python在运行时才会去判断代码正确性
# 这就意味着，当我们需要传入一个对象作为参数时：
# 我们不需要考虑这个对象的编译类型是什么，只要它具有我们需要的属性和方法就可以了，这就是鸭子类型
# “一个对象不需要一定是鸭子，只要它具有鸭子的所有功能和器官，那它就可以是鸭子”
# 例如：
class animal:
    def fly(self):
        print('fly')
class duck():
    def fly(self):
        print('fly')

def make_it_fly(animal):
    animal.fly()
make_it_fly(duck())#duck虽然不是animal的子类，但它具有fly方法，所以可以被make_it_fly函数接受并调用fly方法

# 在java中就不能这样，我们需要把animal定义为一个接口，duck实现这个接口，make_it_fly函数接受一个animal类型的参数，这样就限制了只能传入animal类型的对象，而不能传入其他类型的对象，即使它们具有fly方法也不行