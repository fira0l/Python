from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        self.X_POSITION = 0
        self.Y_POSITION = 0
        super().__init__(shape="circle")
        self.color("White")
        self.penup()
        self.shapesize(stretch_wid=.5,stretch_len=.5)
        self.goto(self.X_POSITION,self.Y_POSITION)

    def move(self):
        new_x = self.xcor()+10
        new_y = self.ycor()+10
        self.goto(new_x, new_y)
