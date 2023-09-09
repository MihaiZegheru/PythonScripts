from turtle import Screen
WIDTH = 800
HEIGHT = 600


class Field:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("Pong")
        self.screen.listen()

    @staticmethod
    def width():
        return WIDTH

    @staticmethod
    def height():
        return HEIGHT

