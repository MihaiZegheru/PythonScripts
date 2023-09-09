from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 14, "bold")
GAME_OVER_FONT = ("Courier", 30, "bold")
FILE_NAME = "data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0

        with open(FILE_NAME, mode='r') as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        text = f"Score: {self.score}   High Score: {self.high_score}"
        self.write(arg=text, move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1

    # def game_over(self):
        # self.goto(0, 0)
        # text = "Game Over"
        # self.write(arg=text, move=False, align=ALIGNMENT, font=GAME_OVER_FONT)

    def reset(self):
        if self.score > self.high_score:
            with open(FILE_NAME, mode='w') as file:
                self.high_score = self.score
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
