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

for state in state_list:
    if answer_state.capitalize() == state:
        new_word = Turtle()
        new_word.hideturtle()
        new_word.penup()
        new_word.goto(int(state_data[state_data.state == state].x), int(state_data[state_data.state == state].y))
        new_word.write(arg=state, font=("Courier", 10, 'normal'))


screen.exitonclick()


