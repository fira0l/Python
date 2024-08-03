from turtle import Turtle
from typing import Tuple


class Paddle(Turtle):

    def __init__(self, X_POSITION, Y_POSITION):
        self.paddle_side = (X_POSITION,Y_POSITION)
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.segments = []
        self.penup()
        self.goto(self.paddle_side)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
