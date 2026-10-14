#绘制奥运五环
import turtle
#第一个圆
turtle.color("blue")
turtle.width(10)
turtle.circle(50)
#第二个圆
turtle.penup()
turtle.goto(80,0)
turtle.pendown()
turtle.color("black")
turtle.circle(50)
#第三个圆
turtle.penup()
turtle.goto(160,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)
#第四个圆
turtle.penup()
turtle.goto(40,-60)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)
#第五个圆
turtle.penup()
turtle.goto(120,-60)
turtle.pendown()
turtle.color("green")
turtle.circle(50)























turtle.done()