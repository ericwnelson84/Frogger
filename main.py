import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import random
import time



screen = Screen()
screen.title("Frogger")
scoreboard = ScoreBoard()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = CarManager()
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    cars.create()
    cars.move()
    for car in cars.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() == 290:
        scoreboard.update()
        cars.level_up()
        player.reset()
    screen.update()

screen.exitonclick()
