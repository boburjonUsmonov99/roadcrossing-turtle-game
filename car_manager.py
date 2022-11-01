from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RAND_SPEED = random.randint(5,8)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars =[]

    def create_car(self):
        ran_suka = random.randint(0,1)
        ran_num = random.randint(0,ran_suka)
        for i in range(0,ran_num):
            car = Turtle("square")

            car.shapesize(stretch_len= 2, stretch_wid = 1)
            color = random.randint(0, 5)
            car.color(COLORS[color])
            rand_y = random.randint(-200, 200)
            car.penup()
            car.goto(300, rand_y)
            self.all_cars.append(car)

    def move_left(self):
        for each_car in self.all_cars:
            new_x = each_car.xcor() - RAND_SPEED
            each_car.goto(new_x, each_car.ycor())






