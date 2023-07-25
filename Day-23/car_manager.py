from turtle import Turtle
from random import randint, choice

COLORS = ["red", "blue", "orange", "yellow", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 1


class CarManager(Turtle):


    def __init__(self):
        self.blocks = []
        self.new_block()
        self.speed = 1


    def new_block(self):
        for i in range(0, randint(1, 6)):
            self.create_block()
    

    def create_block(self):
        block = Turtle(shape="square")
        block.color(choice(COLORS))
        block.shapesize(stretch_len=1, stretch_wid=1)
        block.penup()
        block.goto(x=300, y=randint(-260, 260))
        self.blocks.append(block)


    def move(self):
        for block in self.blocks:
            block.setheading(180)
            block.forward(self.speed)


    def extend(self):
        if self.blocks[-1].xcor() < 240:
            self.new_block()


    def next_level(self):
        self.speed += SPEED_INCREMENT
        print("Speed increased")