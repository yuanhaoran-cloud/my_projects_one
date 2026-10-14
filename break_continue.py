import random
while True:
    a=random.randint(1,101)
    b=int(input("请猜测一个1~100的数："))
    if a==b:
        break
    else:
        print("猜测错误")