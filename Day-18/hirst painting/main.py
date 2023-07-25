import turtle
from turtle import Turtle, Screen
from random import choice

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50),
              (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171),
              (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)
tur = Turtle()
tur.pensize(10)
tur.hideturtle()
tur.penup()
tur.setposition(-250, -250)
for _ in range(10):
    y_cordinate = tur.ycor()
    for _ in range(10):
        tur.dot(20, choice(color_list))
        tur.forward(50)
    y_cordinate += 50
    tur.setposition(-250, y_cordinate)
my_screen = Screen()
my_screen.exitonclick()