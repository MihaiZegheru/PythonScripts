from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
DEFAULT_MOVE_DISTANCE = 5


class Car(Turtle):

    def __init__(self, speed=DEFAULT_MOVE_DISTANCE):
        super().__init__()
        self.speed = speed
        self.penup()
        self.shape("square")
        stretch_len = random.randint(2, 4)
        self.shapesize(stretch_len=stretch_len)
        self.color(random.choice(COLORS))
        self.length = stretch_len

    def move(self):
        self.goto(self.xcor() - self.speed, self.ycor())

    def increment_speed(self, speed):
        self.speed += speed

    def delete(self):
        del self
