from turtle import Turtle
from screen import Field

W_KEY = 'w'
S_KEY = 's'
UP_KEY = 'Up'
DOWN_KEY = 'Down'
MOVE_DISTANCE = 30
OFFSET = 50


class Player(Turtle):

    def __init__(self, position=None, side="default"):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto_start(side)

        self.field = None
        self.up_key = None
        self.down_key = None
        self.set_keys(side)
        self.score = 0

        if position is not None:
            self.goto(position)

    def goto_start(self, side):
        self.set_keys(side)
        screen_half_x = (Field.width() / 2 - OFFSET)
        if side == "left":
            self.goto(x=-screen_half_x, y=0)
        elif side == "right":
            self.goto(x=screen_half_x, y=0)
        elif side == "default":
            return
        else:
            raise Exception("Invalid side.")

    def set_keys(self, side):
        if side == "left":
            self.up_key = W_KEY
            self.down_key = S_KEY
        elif side == "right":
            self.up_key = UP_KEY
            self.down_key = DOWN_KEY
        elif side == "default":
            return
        else:
            raise Exception("Invalid side.")

    def listen(self, field):
        self.field = field
        self.field.screen.onkey(key=self.up_key, fun=self.up)
        self.field.screen.onkey(key=self.down_key, fun=self.down)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        print(self.up_key)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        print(self.down_key)

    @staticmethod
    def offset_to_wall():
        return OFFSET
