from turtle import Turtle


MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.turtle_list = []
        for position in STARTING_POSITION:
            self.new_block(position)
        self.head = self.turtle_list[0]


    def new_block(self, position):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.speed("fast")
        new_turtle.penup()
        new_turtle.setposition(position)
        self.turtle_list.append(new_turtle)


    def extend(self):
        self.new_block(self.turtle_list[-1].position())

    
    def move(self):
        for i in range(len(self.turtle_list)-1, 0, -1):
            x_new = self.turtle_list[i-1].xcor()
            y_new = self.turtle_list[i-1].ycor()
            self.turtle_list[i].goto(x=x_new, y=y_new)
        self.head.forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)