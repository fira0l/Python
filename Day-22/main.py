from turtle import Screen
from Paddel import Paddle


screen = Screen()

screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()