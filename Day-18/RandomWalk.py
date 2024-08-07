from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r, g, b)
    return rgb


directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.title("Random Walk")
screen.exitonclick()
