# python中的动态特性，取决于python的底层维护了一个type类型，所有的class都是type类型的实例。
# 那么这个维护着type类型的type又是什么类型呢？它也是type类型的实例，这就形成了一个循环，python中所有的类型
# 都是type类型的实例，type类型本身也是type类型的实例。
# 这就是python中所谓的元类（metaclass），元类就是用来创建类的类，换句话说，元类就是类的模板，类是元类的实例。

# metaclass是类的模板，所以必须从type类型派生：
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)#cls:当前准备创建的类的对象；name:类的名字；bases:类继承的父类集合；attrs:类的方法集合。
# 在定义类时传入metaclass参数，指定使用ListMetaclass来创建类：
class MyList(list,metaclass=ListMetaclass):
    pass
# 指定metaclass参数后，实例化MyList时，Python解释器会在创建MyList类时调用ListMetaclass的__new__方法，来创建MyList类。
list_custom=MyList()
list_custom.append(1)
list_custom.append(2)
print(list_custom)

