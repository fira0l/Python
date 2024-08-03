import time
from turtle import Screen
from snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard

screen = Screen()


screen.title("The Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


# Created The snake Here
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall
    if snake.head.xcor()>280 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -295:
        game_is_on = False
        score.game_over()

    # Detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    # if head collides with any segment in the tail
    # tirgger game_over

screen.exitonclick()
