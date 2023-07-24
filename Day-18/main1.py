import turtle
from random import randint
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
for i in range(3, 30):
    angle = 360 / i
    no_of_sides = i
    print(angle)
    print(no_of_sides)
    for sides in range(no_of_sides):
        tim.forward(50)
        tim.right(angle)
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))

my_screen = Screen()
my_screen.exitonclick()