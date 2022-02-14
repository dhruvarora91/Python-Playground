from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=-50, starty=50)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True

while game_is_on:

	screen.update()
	time.sleep(0.1)

	snake.move()

	# Detect collision with food.
	if snake.head.distance(food) < 15:
		food.refresh()
		scoreboard.increase_score()
		snake.extend_snake()

	# Detect collision with wall.
	if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
		scoreboard.reset()
		snake.reset()

	# Detect collision with tail.
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			scoreboard.reset()
			snake.reset()
			
screen.exitonclick()
