import random
from turtle import Turtle, Screen
import turtle as t


tim = Turtle()
t.colormode(255)
tim.speed("fastest")


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r, g, b)
    return rgb


def circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(randomcolor())
        tim.circle(100)
        tim.setheading(tim.heading()+10)


circle(5)

# if abs(t.pos()) < 1:
#     break


screen = Screen()
screen.exitonclick()
