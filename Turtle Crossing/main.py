import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

turtle = Player()
car_manager = CarManager()


screen.onkey(key='w', fun=turtle.move_forward)

game_is_on = True
while game_is_on:
    car_manager.generate_car()
    car_manager.move_cars()

    if turtle.check_win():
        car_manager.level_up()
        scoreboard.score += 1
        scoreboard.update()
        car_manager.reset()
        turtle.set_starting_pos()

    if turtle.check_lose(car_manager.cars):
        print("hit")
        scoreboard.game_over()
        game_is_on = False
        # lose

    time.sleep(0.1)
    screen.update()

screen.exitonclick()