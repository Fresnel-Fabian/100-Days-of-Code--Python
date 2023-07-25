from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# setup screen
screen = Screen()
screen.setup(width=600, height=600)
#stop animation
screen.tracer(0)
# initialize player, carmanager, scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
# listen for key stroke
screen.listen()
screen.onkey(fun=player.move, key="w")
# start game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    car_manager.extend()
    # detect collision of block with player
    for block in car_manager.blocks:
        if block.distance(player) < 10:
            screen.clear()
            scoreboard.gameover()
            game_is_on = False
    # detect if the player finish line and increment level
    if player.ycor() > 280:
        scoreboard.update()
        player.restart()
        car_manager.next_level()
screen.exitonclick()