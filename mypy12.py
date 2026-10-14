a=("yuan","hao","ran")
b=(18,19,12,15,31)
c=("teacher","engineer","famer")
# for m in range(min(len(a),len(b),len(c))):
#     print("{0}---{1}---{2}".format(a[m],b[m],c[m]))
# 利用zip（）优化算法
# for a,b,c in zip(a,b,c):
#     print("{0}---{1}---{2}".format(a,b,c))
# d=[x for x in range(1,10000) if x%999==0]
# print(d)
# #同样效果的写法：
# e=[]
# for x in range(1,10000):
#     if x%999==0:
#         e.append(x)
num_cop=[(name,age)for name,age in zip(range(1,101),range(2,99))]
print(num_cop)