from turtle import Turtle


X_POSITION = -385
Y_POSITION = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.segments = []
        self.penup()
        self.goto(X_POSITION, Y_POSITION)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
