import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

        # self.new_x = self.xcor()
        # self.shapesize(stretch_wid=1, stretch_len=2)
        # self.setheading(180)
        # self.penup()
        # self.color(random.choice(COLORS))
        # self.new_y = self.ycor()
        # self.y_position = y_position
        # for i in y_position:
        #     self.goto(300, i)
        # self.move_car()

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # self.forward(STARTING_MOVE_DISTANCE
            # self.new_x -= STARTING_MOVE_DISTANCE
            # self.new_y = self.ycor()
            # self.goto(self.new_x,self.new_y)

