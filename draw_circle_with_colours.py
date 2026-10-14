import turtle
p=turtle.Pen()
a=[x*10 for x in range(1,100)]
p.width(1000000)
my_color=("red","black","yellow","blue","green","orange","purple","cyan")
for c in range(len(my_color)):
    for r in range(0,100,10):
        p.color(my_color[c])
        turtle.circle(r)
        turtle.penup()
        turtle.goto(0,-r)
        turtle.pendown()
turtle.down()


