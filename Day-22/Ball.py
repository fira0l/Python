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
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()