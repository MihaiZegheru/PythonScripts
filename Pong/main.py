from screen import Field
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

field = Field()


player_left = Player()
player_right = Player()
ball = Ball()

scoreboard = Scoreboard()

player_left.goto_start(side="left")
player_right.goto_start(side="right")

player_left.listen(field)
player_right.listen(field)


game_is_playing = True
cont = 0
while game_is_playing:
    if cont > 0:
        cont -= 1

    field.screen.update()

    if ball.detect_wall_collision():
        pass
    elif ball.detect_player_collision(player_left, player_right, (cont == 0)):
        ball.speed_x *= 1.05
        ball.speed_y *= 1.05
        print(ball.speed_y)
        cont = 25

    elif ball.detect_ball_out(player_left, player_right):
        scoreboard.update_score(player_left.score, player_right.score)

    ball.move()


field.screen.exitonclick()