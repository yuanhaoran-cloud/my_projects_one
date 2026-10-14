list_1=[1,2,3]
list2=list_1
print(id(list_1))
print(id(list2))    #没有成功复制一个新的列表
#可行的改变id的复制方式
list3=[]+list_1
print(id(list3))
#遍历列表1的方式
for object in list_1:#别忘了冒号
    print(object)
#列表的排序
#建立新列表的排序
a=[10,20,30,40]
b=sorted(a)   #顺序建立新列表
c=sorted(a,reverse=True) #逆序建立新列表
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
#乱序排列需导入random模组
import random
random.shuffle(a)
print(a)


