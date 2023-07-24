from turtle import Turtle
from random import randint


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()


    def refresh(self):
        x_cor = randint(-280, 280)
        y_cor = randint(-280, 280)
        self.goto(x_cor, y_cor)