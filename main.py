import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

bob = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(bob.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    if bob.ycor() > 280:
        score.increment()
        bob.goto(0, -280)
        car.speed_up()

    for i in car.cars:
        if i.distance(bob) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()