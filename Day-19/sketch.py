from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.back(10)


def right():
    angle = tim.heading()
    angle -= 10
    tim.setheading(angle)


def left():
    angle = tim.heading()
    angle += 10
    tim.setheading(angle)


def clear():
    tim.reset()


def red():
    tim.color("red")


def blue():
    tim.color("blue")


def green():
    tim.color("green")


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=right)
screen.onkey(key="d", fun=left)
screen.onkey(key="c", fun=clear)
screen.onkey(key="1", fun=red)
screen.onkey(key="2", fun=blue)
screen.onkey(key="3", fun=green)
screen.exitonclick()