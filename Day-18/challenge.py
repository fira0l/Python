import turtle
from turtle import Turtle,Screen

tim = Turtle()

angles = []
for i in range(3,11):
    angle_of_polygon = 360 / i
    angles.append(angle_of_polygon)

for angle in angles:
    for i in range(3,11):
        if abs(turtle.pos()) < 1:
            tim.fd(100)
            tim.right(angle)


screen = Screen()
screen.exitonclick()
