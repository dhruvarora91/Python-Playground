import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_player, "w")

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	screen.update()
	car_manager.create_car()
	car_manager.move_car()

	# Detect collision with car
	for car in car_manager.cars:
		if car.distance(player) < 20:
			game_is_on = False
			scoreboard.game_over()

	if player.is_at_finish():
		player.go_to_start()
		scoreboard.next_level()
		car_manager.update_level()

screen.exitonclick()