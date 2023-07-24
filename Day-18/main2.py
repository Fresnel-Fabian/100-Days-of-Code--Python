import turtle
from random import randint
from turtle import Turtle, Screen


turtle.colormode(255)
tur = Turtle()
tur.pensize(10)
for i in range(200):
    tur.color(randint(0, 255), randint(0, 255), randint(0, 255))
    option = randint(0, 4)
    if option == 0:
        tur.forward(50)
    elif option == 1:
        tur.right(90)
        tur.forward(50)
    elif option == 2:
        tur.left(90)
        tur.forward(50)
    else:
        tur.backward(50)

my_screen = Screen()
my_screen.exitonclick()