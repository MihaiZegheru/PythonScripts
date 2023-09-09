from turtle import Turtle, Screen

brush = Turtle()
brush.shape("turtle")
brush.speed(10000)
brush.pensize(4)

screen = Screen()
screen.listen()


def move_forward():
    brush.forward(5)


def move_backwards():
    brush.forward(-5)


def turn_right():
    brush.right(5)


def turn_left():
    brush.left(5)


def clear():
    brush.reset()
    brush.setpos(0, 0)


app_is_playing = True


screen.onkeypress(fun=move_forward, key='w')
screen.onkeypress(fun=move_backwards, key='s')
screen.onkeypress(fun=turn_right, key='d')
screen.onkeypress(fun=turn_left, key='a')
screen.onkeypress(fun=clear, key='c')

screen.exitonclick()
