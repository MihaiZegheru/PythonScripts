from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score(0, 0)

    def update_score(self, score_left, score_right):
        self.clear()
        self.goto(-100, 200)
        self.write(score_left, align="center", font=("Courier", 60, "bold"))
        self.goto(0, 200)
        self.write('-', align="center", font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(score_right, align="center", font=("Courier", 60, "bold"))
