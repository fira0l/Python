class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        status = len(self.question_list)
        return self.question_number < status

    def next_question(self):
        question_item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{question_item.text} (True/False) ")
        self.check_answer(user_answer,question_item.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right!")

        else:
            print("That is Wrong.")
        print(f"The Correct Answer was : {correct_answer}.")
        print(f"Your Current Score is : {self.score}/{self.question_number}")

