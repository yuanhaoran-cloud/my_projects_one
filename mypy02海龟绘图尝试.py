import turtle  #导入模块

turtle.showturtle()              #显示箭头
turtle.forward(300)              #前进多少个像素
turtle.write("袁浩然是大帅哥")      #所写内容
turtle.color("blue")             #画笔的颜色，注意括号内要打引号
turtle.left(120)                 #箭头左转多少度
turtle.forward(150)
turtle.goto(0,-100)           #画笔直线前往某个坐标
turtle.penup()                   #抬起笔，即不显示轨迹
turtle.goto(50,-150)          #承接上面抬起笔的前提下，箭头移动
turtle.pendown()                 #落笔以显示路径
turtle.circle(90)                #以箭头所处角度为切向，做一个半径为90的圆

turtle.done()    #保持结束窗口不关闭，便于观察效果