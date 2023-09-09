from turtle import Turtle, Screen
import random


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("SlateBlue3")
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")


startX = -470
startY = -250
space = 95

endX = 470


def setup_turtle(new_turtle, new_color):
    global startY
    new_turtle.color(new_color)
    new_turtle.shapesize(stretch_wid=2.5, stretch_len=2.5)
    new_turtle.penup()
    new_turtle.goto(x=startX, y=startY)
    startY += space

    return new_turtle


for color in colors:
    turtle = Turtle(shape="turtle")
    turtles.append(setup_turtle(turtle, color))


winner = None
all_finished = False

while all_finished is False:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() >= endX:
            if winner is None:
                winner = turtle
            turtle.goto(y=turtle.ycor(), x=475)
            turtles.remove(turtle)

        if not turtles:
            all_finished = True


color = winner.color()

if color[1] == user_bet:
    print(f"You guessed right! The {user_bet} turtle won!")
else:
    print(f"You lost the bet! The {color[1]} turtle won!")


screen.exitonclick()
