from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create()

    def create(self):
        random_chance = random.randint(1,6)
        random_y = random.randint(-230, 250)
        if random_chance == 1:
            self.hideturtle()
            #when creating multiple objects from inherted classed. you have to use the inherited class name.
            # in this case new_car = Turtle(). When using inheritance on creating single objects its not necessary.
            # Like for the scoreboard objects
            new_car = Turtle("square")
            new_car.penup()
            new_car.goto(300, random_y)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=0.5, stretch_len=2)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT