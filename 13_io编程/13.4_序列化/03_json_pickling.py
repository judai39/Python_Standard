# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
# 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
# 也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且
# 可以直接在Web页面中读取，非常方便。
import json
import pickle

# 1.json序列化存储数据类型为pyhon对象
dict_json=dict(name="Bob",age=20,score=8)
dict_list=list(("bob","20","14"))
# 使用json模块内置dumps方法序列化为json对象
json_picle1=json.dumps(dict_json)
json_picle2=json.dumps(dict_list)#list也可以通过json.dumps()序列化
print(json_picle1)
print(json_picle2)
# 也可以使用dump()序列化为file-like Object

# 使用json模块内置loads方法反序列化python对象
json_str=json.loads(json_picle1)
print(json_str)

# 2.json序列化实例化对象为python对象
class student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    
def student_to_dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
json_student=json.dumps(student_to_dict(student("小明",2,329)))
print(json_student)
student=json.loads(json_student)
print(student)

