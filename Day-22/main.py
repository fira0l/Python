from turtle import Screen
from Paddel import Paddle


screen = Screen()

screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(-385, 0)
right_paddle = Paddle(385,0)

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()