from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index in range(len(question_data)):
	question_bank.append(Question(question_data[index]['text'], question_data[index]['answer']))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
	quiz.next_question()

print(f"Quiz completed. Your final score is {quiz.score}/{quiz.question_number}.")