import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from game_over import Game_over

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

animal = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(animal.move_forward, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_left()
    screen.update()

    for car_a in car.all_cars:
        if car_a.distance(animal) < 20 :
            game_is_on = False
            game_over = Game_over()

    if animal.ycor() > 260:
        scoreboard.add_point()
        animal.new_level()

screen.exitonclick()
