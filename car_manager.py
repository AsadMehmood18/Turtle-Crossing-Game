from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.penup()
            color = choice(COLORS)
            new_car.color(color)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_y = randint(-250, 250)
            new_car.goto(300, new_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT



