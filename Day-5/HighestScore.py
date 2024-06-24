students_score = input("Insert Your Marks: ").split()

for i in range(0,len(students_score)):
    students_score[i]=int(students_score[i])

largest = students_score[0]

for mark in students_score:
    if mark > largest:
        largest = mark
print(f"The highest score in the class is: {largest}")
    