from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.set_starting_pos()

    def set_starting_pos(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def check_win(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def check_lose(self, cars):
        for car in cars:
            if car.ycor() - 27 < self.ycor() < car.ycor() + 27:
                if car.xcor() + car.length * 13 > self.xcor() > car.xcor() - car.length * 13:
                    return True
        return False
