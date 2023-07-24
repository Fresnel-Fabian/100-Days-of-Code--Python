import turtle

t1 = turtle.Turtle()
print(t1)
t1.shape("turtle")
t1.color("Blue")
for i in range(12):
    t1.forward(100)
    t1.right(30)
my_screen = turtle.Screen()
my_screen.canvwidth
my_screen.exitonclick()