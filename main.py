import turtle
from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("50_states.csv")

t = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
all_states = data.state.to_list()
states_guessed = []
while len(states_guessed) < 50:
    answer_user = screen.textinput(title=f"{len(states_guessed)}/50 States Correct",
                                   prompt="What's another State name? ").title()

    if answer_user == "Exit":
        missing_states = [state for state in all_states if state not in states_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_user in all_states:
        states_guessed.append(answer_user)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_user]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_user)



screen.mainloop()
