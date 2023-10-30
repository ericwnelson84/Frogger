from turtle import Turtle
from player import Player
from car_manager import CarManager

FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.pencolor("black")
        self.write(arg=f"Level {self.level}, Score: {self.score} ", align="left", font=FONT)

    def update(self):
        self.score += 1
        self.level += 1
        self.penup()
        self.goto(-270, 260)
        self.clear()
        self.write(arg=f"Level {self.level},Score: {self.score} ", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.pencolor("red")
        self.write(arg=f"GAME OVER ", align="center", font=("Arial", 15, "normal"))
