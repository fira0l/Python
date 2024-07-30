from data import question_data
from question_model import Question


question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

#     for keys in questions:
#         question = Question(keys,questions[keys])
#         question_bank.append(question)
# for i in range(0,len(question_bank)-1):
#     print(question_bank[i].text)
