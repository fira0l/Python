from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xposition, yposition):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(xposition, yposition)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
