import turtle as tr
import random
tr.colormode(255)
tr.hideturtle()
tr.penup()
tr.setheading(230)
tr.forward(280)
tr.setheading(0)
tr.speed("fastest")
rgb_color = [(251, 251, 248), (254, 240, 252), (212, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]
scr=tr.Screen()
for i in range(0,10):
    for j in range(0,10):
        tr.pendown()
        tr.dot(20,random.choice(rgb_color))
        tr.penup()
        tr.forward(50)   
    tr.setheading(90)
    tr.forward(50)
    tr.setheading(180)
    tr.forward(500)
    tr.setheading(0)         
scr.exitonclick()