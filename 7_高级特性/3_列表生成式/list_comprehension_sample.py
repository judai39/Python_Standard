# 通过列表生成式快速创捷列表

# [1,2,3,4,...]
list(range(1,11)) 

# [1x1,2x2,3x3,4x4...]
[x*x for x in range(1,11)]

# [a+A,b+B,c+C...]
[m+n for m in 'abc' for n in 'ABC']

# [key1=value1,key2=value2...]
[k+'='+v for k,v in {'key1':'value1','key2':'value2'}.items()]

# 引入逻辑判断
# if...else
[x for x in range(1,11) if x>10]#加else会报错，后if...是过滤器

# 
[x if x>5 else 10000 for x in range(1,11)]#加else不会报错，前if为x的过滤后赋值结果，一定要有值