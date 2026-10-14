import io  #导入可变字符串库
Immutabe_String="abcdefghijklmnopqrstuvwxyz"  #常规的不可变字符串
Mutable_String=io.StringIO(Immutabe_String)  #新建一个可变字符串并索引值
print(Mutable_String.getvalue())    #打印可变字符串的索引值
print("id1="+str(id(Mutable_String)))  #易错点：注意加号前后应为同类型
Mutable_String.seek(4)    #指针移到可变字符串索引值的对应序列位置
Mutable_String.write("你好")  #从该位置开始书写新内容以替换原内容
print(Mutable_String.getvalue())
print("id2="+str(id(Mutable_String))) 
#对比前后id可知：可变字符串更改后不会生成一个新的id