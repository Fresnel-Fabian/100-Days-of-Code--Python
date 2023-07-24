import turtle
from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(500, 400)
turtle.penup()
user_input = screen.textinput(title="Bet", prompt="Which turtle will win ?")
colors = ["red", "orange", "blue", "purple", "yellow", "green"]
y = 120
turtle_list = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y -= 40
    turtle_list.append(new_turtle)

if user_input:
    is_game_on = True

while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_game_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_input:
                print(f"You won. Wining color is {wining_color}")
            else:
                print(f"You lose. Wining color is {wining_color}")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()