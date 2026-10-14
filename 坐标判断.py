x=int(input("请输入x坐标："))
y=int(input("请输入y坐标："))
if (x==0 and y==0):
    print("在原点")
elif (x==0):
    print("在y轴")
elif (y==0):
    print("在x轴")
elif (x>0 and y>0):
    print("在第一象限")
elif (x>0 and y<0):
    print("在第四象限")
elif (x<0 and y>0):
    print("在第二象限")
else:
    print("在第三象限")

