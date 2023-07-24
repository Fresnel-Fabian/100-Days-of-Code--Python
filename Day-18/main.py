from turtle import Turtle, Screen


tur = Turtle()
tur.shape("turtle")
tur.color("yellow")
for i in range(15):
    tur.forward(10)
    tur.penup()
    tur.forward(10)
    tur.pendown()
my_screen = Screen()
my_screen.exitonclick()
