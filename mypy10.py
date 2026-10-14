a=(1,2,3)
b=1,2,3
c=(1,)#只有一个元素的元组需要打逗号，否则会直接转换成整数
d=(1)
print(type(a))
print(type(b))
print(type(c))  #class"type"
print(type(d))  #class"int"
e=tuple()  #创建一个空元组
f=tuple("abc")  #仿照list（）创建列表   利用tuple（）创建元组
g=tuple([1,2,3])
k=tuple(range(3))
print(e)
print(f)
print(g)
print(k)
