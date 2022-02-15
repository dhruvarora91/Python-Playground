from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	# Collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Collision with r_paddle
	if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
		ball.bounce_x()

	# right paddle misses the ball
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.l_point()

	# left paddle misses the ball
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.r_point()

screen.exitonclick()