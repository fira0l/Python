from turtle import Screen
from Paddel import Paddle
from Ball import Ball
from Scoreboard import ScoreBoard
import time


screen = Screen()

screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350,0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs To Bounce
        ball.bounce_y()

    # Detect Collision with Paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.lpoint()

    if ball.xcor() < -380:
        ball.reset_position()
        score.rpoint()

screen.exitonclick()
