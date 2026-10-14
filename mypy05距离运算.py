import turtle
import math
x1,y1=100,100
x2,y2=140,-100
x3,y3=50,80
x4,y4=-40,-100
x5,y5=10,100
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
turtle.goto(x5,y5)
#计算距离
distance=math.sqrt((x5-x1)**2+(y5-y1)**2)#计算距离需引入数学模块
print("距离是"+str(distance))  #在代码执行界面显示距离
turtle.write("距离是"+str(distance))  #在海龟绘图界面显示距离
turtle.done()  #保持程序结束后等待

