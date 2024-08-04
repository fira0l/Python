import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Create Screen
screen = Screen()
screen.title("The Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create The Turtle
player = Player()
car = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()




# Move Cars along the Screen
# Detect Collision with cars
# Detect When The Turtle passes the End-line
# speed-up the cars every success-full cross
# Manage the score
