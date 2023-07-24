import turtle
from random import randint
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def draw_spirography(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


angle = int(input("Enter the size of gap: "))
draw_spirography(angle)
my_screen = Screen()
my_screen.exitonclick()
