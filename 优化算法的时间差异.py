import time
start_1=time.time()
result=[]
for i in range(100):
    for m in range(100):
        sum=i*10000+m*1000
        result=result+[sum*100000]
end_1=time.time()
print("总耗时："+str(float(end_1)-float(start_1)))
start_2=time.time()
for i in range(100):
    for m in range(100):
        sum = i * 10000 + m * 1000
        result.append(sum*100000)
end_2=time.time()
print("总耗时："+str(float(end_2)-float(start_2)))