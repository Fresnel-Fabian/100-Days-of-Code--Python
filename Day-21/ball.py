from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1


    def move(self):
        xcor = self.xcor() + self.xmove
        ycor = self.ycor() + self.ymove
        self.goto(x=xcor, y=ycor)

    
    def y_bounce(self):
        self.ymove *= -1

    
    def x_bounce(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.x_bounce()