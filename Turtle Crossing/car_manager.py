from car import Car
import random


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
SPAWNING_X = 310
DESTROYING_X = -350


class CarManager:

    def __init__(self):
        self.cars = []
        self.starting_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if random.randint(1, 7) == 5:
            speed = random.randint(self.starting_speed, 2 * self.starting_speed)
            new_car = Car(speed)

            new_car.goto(SPAWNING_X, random.randint(-240, 240))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < DESTROYING_X:
                self.cars.remove(car)
                car.delete()

    def level_up(self):
        for car in self.cars:
            car.increment_speed(MOVE_INCREMENT)
        self.starting_speed += MOVE_INCREMENT

    def reset(self):
        for car in self.cars:
            car.goto(-1000, -1000)
            car.delete()
            self.cars.remove(car)
