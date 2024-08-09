import pandas,turtle


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# print(data)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another State's name?").title()

    all_state = data.state.to_list()

    if answer_state == "Exit":
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# users_choice = data[data.state == answer_state]
# xcor = users_choice["x"]
# ycor = users_choice["y"]

item_to_write = ""
for item in all_state:
    if item not in guessed_states:
        item_to_write = item_to_write + "\n" + item
        with open("states_to_learn", mode="w") as writee:
            writee.write(item_to_write)


# print(xcor,ycor)
# if data[data.state] in guessed_states:
#     with open("states_to_learn", mode="w") as write:
#         write.write(data[data.states])
# states_to_learn.csv