from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
user1 = Paddle(xcor=-380)
user2 = Paddle(xcor=380)
scoreboard_1 = Scoreboard(xcor=-200, id=1)
scoreboard_2 = Scoreboard(xcor=200, id=2)
ball = Ball()
screen.listen()
screen.onkey(fun=user1.up, key="w")
screen.onkey(fun=user1.down, key="s")
screen.onkey(fun=user2.up, key="Up")
screen.onkey(fun=user2.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    # detect collision with paddle
    if user2.distance(ball) < 50 and ball.xcor() > 320:
        ball.x_bounce()
    if user1.distance(ball) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard_1.update()
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard_2.update()
    if scoreboard_1.score > 10:
        scoreboard_1.gameover()
        game_is_on = False
    if scoreboard_2.score > 10:
        scoreboard_2.gameover()
        game_is_on = False
screen.exitonclick()