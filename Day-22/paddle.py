from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, xcor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(xcor, 0)
        

    def up(self):
        if self.ycor() < 280:
            new_ycor = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_ycor)

        
    def down(self):
        if self.ycor() > -280:
            new_ycor = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_ycor)