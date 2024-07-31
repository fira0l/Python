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


directions = [0, 90, 180, 270]


for direction in range(1000):
    tim.color(randomcolor())
    tim.circle(100)
    tim.setheading(direction)
    # if abs(t.pos()) < 1:
    #     break


screen = Screen()
screen.exitonclick()
