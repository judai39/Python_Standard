# 对于一个完整的继承体系，如果我们想要引入一个新的继承关系，
# 那么我们需要修改所有相关的类，这样会导致代码的可维护性变差。
# 为了解决这个问题，我们可以使用多重继承来实现更灵活的继承关系。
# 使用MaxIn
class animal:
    pass
class mammal(animal):
    pass
class bird(animal):
    pass

class dog(mammal):
    pass
# 蝙蝠
class bat(mammal):
    pass
# 鹦鹉
class parrot(bird):
    pass
# 鸵鸟
class ostrich(bird):
    pass

# 现在引入runnabale_maxin和flyale_maxin两个类，可以使用多重继承
# 尽量不要单独实例化maxin类
class runnable_maxin:
    def run(self):
        print("Running")
class flyable_maxin:
    def fly(self):
        print("Flying")

class new_bat(mammal, flyable_maxin):
    pass
class new_parrot(bird, flyable_maxin):
    pass
class new_ostrich(bird, runnable_maxin):
    pass
class new_dog(mammal, runnable_maxin):
    pass

if __name__ == '__main__':
    new_bat().fly()
# 在有关java中，多重继承是通过接口来实现的。（java类只能单继承）