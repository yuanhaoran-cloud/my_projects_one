# for x in range(1,6):
#     print(str(x)*5,end="\t")

# for x in range(1,6):
#     for y in range(1,6):
#         print(x,end="\t")
#     print("\t")
#

for i in range(1,10):
    for x in range(1,i+1):
        result=i*x
        print("{0}*{1}={2}".format(i,x,result),end="\t")
    print("\t")


#进一步选择结果大于50的数据
for i in range(1,10):
    for x in range(1,i+1):
        result=i*x
        if result>50:
            print("{0}*{1}={2}".format(i,x,result),end="\t")
    print("\t")
