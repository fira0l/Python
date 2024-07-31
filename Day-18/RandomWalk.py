from turtle import Turtle, Screen
import random


colours = ["dodger blue", "spring green", "firebrick", "tomato", "chocolate",
           "midnight blue", "magenta", "khaki"]

tim = Turtle()
tim.pensize(15)
tim.speed("fastest")

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(50)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.title("Random Walk")
screen.exitonclick()
