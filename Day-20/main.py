from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
score = 0
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()
    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.ycor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # detect collision with tail
    for block in snake.turtle_list[1:]:
        if snake.head.distance(block) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()