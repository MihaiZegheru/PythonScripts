from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-230, 250)
        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
