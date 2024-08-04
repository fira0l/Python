from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create The Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # Move The Turtle across the screen

    def move_up(self):
        self.forward(MOVE_DISTANCE)


