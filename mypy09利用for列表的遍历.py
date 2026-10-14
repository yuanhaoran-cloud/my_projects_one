# a = [
#     ["袁",18,"快乐"],
#     ["浩",19,"帅气"],
#     ["然",20,"完美"]
# ]
# for m in range(3):  #行与列均从0开始计数,但是range包头不包尾
#     for n in range(3):
#         print(a[m][n],end="\t")
#     print()#注意区分中英式双引号不一样#每一行末尾要有逗号
#
# a={"name":"yuanhaoran","age":18}
# for x in  a.items():
#     print(x )


# for x in range(0,1000000,99):
#     print(x,end="\t")

# sum=0
# for x in range(1,101):
#     sum+=x
# print(sum)
#
# odd_num=0
# for i in range(0,101,2):
#     odd_num+=i
# print(odd_num)
#
# even_num=0
# for t in range(1,101,2):
#     even_num+=t
# print(even_num)
sum=0
sum_odd=0
sum_even=0
for i in range(1,10001):
    sum+=1
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print("总和是{0}，奇数和是{1}，偶数和是{2}".format(sum,sum_odd,sum_even))
