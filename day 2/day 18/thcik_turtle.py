import turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
moves=[0,90,180,270,360]
death=turtle.Turtle()
turtle.colormode(255)
def rando_rgb():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)
screen=turtle.Screen()
death.speed(0)
for i in range(800):
    
    death.pensize(10)
    death.setheading(random.choice(moves))
    death.forward(20)
    death.color(rando_rgb())


screen.exitonclick()