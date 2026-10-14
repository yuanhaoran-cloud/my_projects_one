import time

#加法连接符的运算速度计算
time1=time.time()
a=""
for i in range(100000):
    a+="sxt"
time2=time.time()
print("加法的时间为"+str(time2-time1))


#join连接符的运算时间
time3=time.time()
b=[]
for i in range(100000):
    b.append("sxt")
b="".join(b)
time4=time.time()
print("join的运算时间"+str(time4-time3))
