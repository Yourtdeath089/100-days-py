import turtle
death=turtle.Turtle()
screen=turtle.Screen()
death.shape("turtle")
# for i in range(4):
#     death.forward(100)
#     death.penup()
#     death.right(90)
#     death.pendown()
# death.penup()
# death.backward(100)
# for i in range(15):
#     death.forward(10)
#     death.penup()
#     death.forward(10)
#     death.pendown()


death.right(60)
death.forward(100)
death.right(120)
death.forward(100)
death.right(120)
death.forward(100)
death.right(60)
on= True
i=4
import random
# A simple list of the most common core colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
col=random.choices(colors)
# print(col)
while on is True:
    
    for f in range(i):
        death.color(col)
        angle_move=360//i
        death.forward(100)
        death.right(angle_move)
    col=random.choices(colors)
        
    
    i+=1
    if i==9:
        on=False
    # for f in range(i):
    #     angle_move=360//i
    #     death.forward(100)
    #     death.right(angle_move)
    # on=False
    
screen.exitonclick()