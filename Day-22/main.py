from turtle import Screen
from Paddel import Paddle


screen = Screen()

screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

paddle = Paddle()

screen.listen()
screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)


screen.exitonclick()