from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:



    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Quiz App",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        image2 = PhotoImage(file="images/false.png")
        self.false_button = Button(image=image2, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.quiz.check_answer("True")

    def false_pressed(self):
        self.quiz.check_answer("False")
