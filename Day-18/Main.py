from turtle import Turtle, Screen
# import heroes
tim = Turtle()
tom = Turtle()
tom.shape("turtle")
tim.shape("turtle")
tim.color("cyan", "black")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

for step in range(15):
    for step in ("black","white"):
        tim.pencolor(step)
        tim.forward(10)
tim.pencolor("black")
tim.right(135)
tim.forward(10)
tim.right(180)
tim.forward(10)
tim.left(90)
tim.forward(10)
tim.penup()
tim.goto(0,0)
# print(heroes.gen())


#Teachers Way
tom.penup()
tom.goto(0,50)
tom.pendown()
for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.fd(10)
    tom.pendown()






















screen = Screen()
screen.exitonclick()