from turtle import Turtle
FONT = ('Fira Code', 24, 'normal')


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.hideturtle()
		self.penup()
		self.write_score()

	def write_score(self):
		self.clear()
		self.goto(0, 270)
		self.write(f"Score: {self.score}", move=False, align='center', font=FONT)

	def game_over(self):
		self.clear()
		self.goto(0, 0)
		self.write(f"Game Over. Your final score: {self.score}", move=False, align='center', font=FONT)

	def increase_score(self):
		self.score += 1
		self.write_score()
