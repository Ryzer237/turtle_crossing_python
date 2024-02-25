import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
screen.bgcolor("black")
screen.listen()
car=CarManager()
scoreboard=Scoreboard()
screen.onkey(player.up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()
    for cars in car.all_cars:
        if cars.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    if player.check_finsih():
        player.go_back()
        car.increase_speed()
        scoreboard.increase_level()
screen.exitonclick()