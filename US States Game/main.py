import turtle
import pandas

IMAGE = "blank_states_img.gif"
guessed_states = []


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.addshape(IMAGE)
turtle.shape(IMAGE)


data = pandas.read_csv("50_states.csv")
states = data.state

all_states = states.tolist()

score = 0
max_score = 50

while score < max_score:
    answer_state = screen.textinput(title=f"{score}/{max_score} States Correct", prompt="Name a state:").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state in guessed_states:
            continue
        index = data[states == answer_state].index[0]
        guessed_states.append(answer_state)
        score += 1
        x_coord = int(data[states == answer_state].x)
        y_coord = int(data[states == answer_state].y)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=x_coord, y=y_coord)
        t.write(answer_state)


screen.exitonclick()
