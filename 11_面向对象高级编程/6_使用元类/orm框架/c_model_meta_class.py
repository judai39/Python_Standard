from b_filed import Field

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        # 排除掉对Model类的修改
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        # 遍历实例类的所有成员
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系（mappings属性为dict字典中维护的对象，也就是说，__new__方法中动态的添加实例化一个类dict对象的方法了）
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
    
class Model(dict, metaclass=ModelMetaClass):
    # 定义所有的ORM映射关系（**kw意为传入不确定的参数集）
    def __init__(self,**kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))