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
        self.go_to_start()
        self.setheading(90)

    # Move The Turtle across the screen

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


