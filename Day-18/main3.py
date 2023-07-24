import turtle
from random import choice, randint
from turtle import Turtle, Screen


direction = [0, 90, 180, 270]
turtle.colormode(255)
tur = Turtle()
tur.pensize(5)
tur.speed("fastest")
for _ in range(4000):
    tur.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tur.setheading(choice(direction))
    tur.forward(10)
    
my_screen = Screen()
my_screen.exitonclick()