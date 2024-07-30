from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    print("\n")

print("You Have Completed the quiz")
print(f"Your Final score is :{quiz.score}/{quiz.question_number}")
#     for keys in questions:
#         question = Question(keys,questions[keys])
#         question_bank.append(question)
# for i in range(0,len(question_bank)-1):
#     print(question_bank[i].text)
