import pandas,turtle


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# print(data)


answer_state = screen.textinput(title="Guess A State", prompt="What's another State's name?").title()


screen.exitonclick()
