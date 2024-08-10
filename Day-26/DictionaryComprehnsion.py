# dictionary comprehension from lists
# new_dict = {new_key : new_Value for item in list}
import random

names = ["Alex", "Beth", "Firaol", "Dave", "Eleanor", "Freda"]

students_score = {names : random.randint(50,100) for names in names}
print(students_score)

# dictionary comprehension from dictionary
# new_dict = {new_key : new_value for (key,value) in dict.items()}

passed_stuents = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_stuents)
# dictionary comprehension from dictionary with condition
# new_dict = {new_key: new_value for (key, value) in dict.item() if test}

