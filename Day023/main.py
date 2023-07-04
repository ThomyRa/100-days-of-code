import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("The turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

counter = 0
game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.turtle_crossed():
        player.go_to_start()
        car_manager.lvl_up()
        scoreboard.increase_lvl()

screen.exitonclick()
