from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
