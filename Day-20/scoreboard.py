from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=280)
        self.update()

    
    def update(self):
        self.clear()
        self.write(arg=f"score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1


    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GameOver", align=ALIGNMENT, font=FONT)