from turtle import Turtle
from screen import Field
from player import Player

SPEED_X = 0.13
SPEED_Y = 0.13
COLLISION_OFFSET = 5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed_x = SPEED_X
        self.speed_y = SPEED_Y

    def move(self):
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y
        self.goto(new_x, new_y)

    def detect_wall_collision(self):
        height_limit = Field.height() / 2 - COLLISION_OFFSET
        if self.ycor() > height_limit or self.ycor() < -height_limit:
            self.speed_y *= -1
            return True
        return False

    def detect_player_collision(self, player_left, player_right, detect):
        width_limit = Field.width() / 2 - Player.offset_to_wall() - 20
        if width_limit < self.xcor() < width_limit + 5 and detect:
            if self.distance(player_right) < 50:
                self.speed_x *= -1
                return True
        elif -width_limit - 5 < self.xcor() < -width_limit and detect:
            if self.distance(player_left) < 50:
                self.speed_x *= -1
                return True
        return False

    def detect_ball_out(self, player_left, player_right):
        global SPEED_X, SPEED_Y
        width_limit = Field.width() / 2 - 10
        if self.xcor() > width_limit:
            self.reset_position()
            player_left.score += 1
            SPEED_X = -abs(SPEED_X)
            return True
        elif self.xcor() < -width_limit:
            self.reset_position()
            player_right.score += 1
            SPEED_X = abs(SPEED_X)
            return True
        return False

    def reset_position(self):
        self.speed_x = SPEED_X
        self.speed_y = SPEED_Y
        self.goto(0, 0)

