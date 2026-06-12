import turtle as t
import random
death=t.Turtle()
death.shape("turtle")
sc=t.Screen()
t.colormode(255)
def rando_rgb():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)
f=0
for i in range(360):
    death.speed(0)
    death.color(rando_rgb())
    death.circle(100)
    death.right(f)
    f+=1



sc.exitonclick()