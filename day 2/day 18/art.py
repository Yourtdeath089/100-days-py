# import colorgram
# colors = colorgram.extract("day 2/day 18/images.jpg", 30)
# new_color=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     lsit=(r,g,b)
#     new_color.append(lsit)
# print(new_color)
















rigged=[(228, 240, 235), (241, 119, 38), (240, 77, 93), (163, 111, 8), (212, 152, 162), (131, 215, 207), (239, 96, 29), (167, 45, 137), (28, 35, 41), (85, 183, 6), (53, 93, 86), (148, 185, 222), (134, 216, 221), (249, 207, 0), (201, 134, 13), (247, 210, 40), (133, 197, 171), (158, 192, 229), (233, 165, 177), (43, 77, 72), (88, 94, 98), (240, 171, 156), (27, 39, 37), (145, 28, 113), (119, 97, 0), (116, 136, 137)]

import random
import turtle as t
death=t.Turtle()
screen=t.Screen()
t.colormode(255)
death.speed(0)
death.penup()
def dots_line():
    global rigged
    for i in range (11):
        death.forward(50)
        death.color(random.choice(rigged))
        death.dot(15)
s=-255
for i in range(10):
    death.goto(-255,s)
    death.dot(15)
    s+=50
    dots_line()
screen.exitonclick()












