from turtle import Turtle


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []


class Snake:
    for position in starting_positions:
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)

    def move(self):
        # Made The Snake Segments to Follow Each other
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)