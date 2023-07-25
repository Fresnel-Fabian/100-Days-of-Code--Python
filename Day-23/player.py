from turtle import Turtle
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = (0, 280)
MOVE_DISTANCE = 10


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(270)


    def move(self):
        ycor = self.ycor() + MOVE_DISTANCE
        self.goto(x=0, y=ycor)


    def restart(self):
        self.goto(STARTING_POSITION)