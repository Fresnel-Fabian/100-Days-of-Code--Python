from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self, xcor, id):
        super().__init__()
        self.score = 0
        self.id = id
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=xcor, y=270)
        self.update()

    
    def update(self):
        self.clear()
        self.write(arg=f"Player: {self.id} Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def gameover(self):
        self.goto(0, 0)
        self.write(arg=f"Player {self.id} wins", align=ALIGNMENT, font=FONT)