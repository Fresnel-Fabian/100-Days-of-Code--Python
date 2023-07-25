from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=-260, y=260)
        self.level = 0
        self.color("black")
        self.update()

    
    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        self.level += 1
    

    def gameover(self):
        self.goto(0, 0)
        self.write(arg=f"GameOver \nLevel: {self.level}", align="center", font=FONT)
        