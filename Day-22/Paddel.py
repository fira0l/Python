from turtle import Turtle


X_POSITION = -435
Y_POSITION = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color("white")
        self.segments = []
        self.penup()
        self.goto(X_POSITION,Y_POSITION)

    def up(self):
        self.setheading(90)
        self.forward(10)

    def down(self):
        self.setheading(270)
        self.forward(10)
