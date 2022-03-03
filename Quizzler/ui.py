from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
  
  def __init__(self, quiz_brain: QuizBrain):
    
    self.quiz_brain = quiz_brain
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    
    # Canvas
    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text(
      150,
      125,
      text="Some Question Text",
      width=280,
      fill=THEME_COLOR,
      font=("Arial", 20, "italic")
    )
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
    # Score Label
    self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
    self.score_label.grid(row=0, column=1)
    
    # True Button
    true_image = PhotoImage(file="images/true.png")
    self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
    self.true_button.grid(row=2, column=0)
    
    # False Button
    false_image = PhotoImage(file="images/false.png")
    self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_passed)
    self.false_button.grid(row=2, column=1)
    
    self.get_next_question()
    
    self.window.mainloop()
  
  def get_next_question(self):
    self.canvas.config(bg="white")
    if self.quiz_brain.still_has_questions():
      self.score_label.config(text=f"Score: {self.quiz_brain.score}")
      q_text = self.quiz_brain.next_question()
      self.canvas.itemconfig(self.question_text, text=q_text)
    else:
      self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")
  
  def true_pressed(self):
    self.give_feedback(self.quiz_brain.check_answer("true"))
  
  def false_passed(self):
    is_right = self.quiz_brain.check_answer("false")
    self.give_feedback(is_right)
  
  def give_feedback(self, is_right: bool):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, func=self.get_next_question)
