import time
from turtle import Turtle,Screen
from snake import Snake

screen = Screen()

screen.title("The Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


# Created The snake Here
snake = Snake()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()








screen.exitonclick()
