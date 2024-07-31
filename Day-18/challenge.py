import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()

# angles = []
# for i in range(3,11):
#     angle_of_polygon = 360 / i
#     angles.append(angle_of_polygon)
#
# for angle in angles:
#     for i in range(3,11):
#         if abs(turtle.pos()) < 1:
#             tim.fd(100)
#             tim.right(angle)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_side):
    for _ in range(num_side):
        angle = 360 / num_side
        tim.fd(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
