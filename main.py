import pandas
import csv
from turtle import Turtle, Screen

screen = Screen()
t = Turtle()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()


answer_state = screen.textinput(title="Guess the State!", prompt="What's another state?")
correct_state_count = 0

while correct_state_count <= 50:
    for state in state_list:
        if answer_state.title() == state.title():
            correct_state_count += 1
            new_word = Turtle()
            new_word.hideturtle()
            new_word.penup()
            new_word.goto(int(state_data[state_data.state == state].x), int(state_data[state_data.state == state].y))
            new_word.write(arg=state, font=("Courier", 10, 'normal'))
    answer_state = screen.textinput(title=str(correct_state_count) + "/50 states correct",
                                    prompt="What's another state?")

print("Hooray! You've correctly guessed all 50 states!")

screen.exitonclick()


