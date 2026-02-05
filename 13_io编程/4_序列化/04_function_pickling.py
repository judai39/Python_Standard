import pickle

# 序列化方法

# 1.序列化普通方法
def print_score():
    print("90分")
    # return 90

function_pickling_obj=pickle.dumps(print_score)
print(pickle.loads(function_pickling_obj))

# 2.序列化lamda匿名方法(无法正常序列化匿名方法，可以通过转化成普通方法进行序列化)
# lambda_pickling=pickle.dumps(lambda a,b:a*b)
# print(pickle.loads(lambda_pickling))
# PicklingError: Can't pickle <function <lambda> at 0x000001269A229080>

# 2*.转化为普通方法进行序列化
def return_lambda(a,b):
    return a*b
lambda_pickling=pickle.dumps(return_lambda)
print(pickle.loads(lambda_pickling))