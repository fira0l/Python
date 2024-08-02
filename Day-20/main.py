from turtle import Turtle,Screen

screen = Screen()

screen.title("The Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)








screen.exitonclick()
