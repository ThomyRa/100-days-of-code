from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_chance = random.randint(1, 6)
        if car_chance == 1:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(range(-250, 250, 20))
            new_car.goto(300, random_y)
            new_car.showturtle()
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT
