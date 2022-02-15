import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

# Adding image as the background
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data['state'].to_list()

guessed_states = []

while len(guessed_states) < 50:

  answer_state = screen.textinput(f"{len(guessed_states)}/50 Guess the state", "What's another state name?").title()

  if answer_state == 'Exit':
    unguessed_states = []
    for state in states_list:
      if state not in guessed_states:
        unguessed_states.append(state)

    pandas.DataFrame(unguessed_states).to_csv("unguessed_states.csv")
    break

  if answer_state in states_list:
    guessed_states.append(answer_state)
    state_row = data[data['state'] == answer_state]

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(state_row.x), int(state_row.y))
    t.write(state_row.state.item(), align="center", font=("Courier", 12, "normal")) 
