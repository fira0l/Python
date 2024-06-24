students_heights = input("Input Heights you want to Find the average for:(in cm) separated by ', ':  ")
students_heights = students_heights.split()

avg = 0
total = 0
counter = 0
for i in range(0,len(students_heights)):
    counter+=1
    students_heights[i]= int(students_heights[i])
    total += students_heights[i]
# avg = total/len(students_heights)
avg = total/counter
print(round(avg))
    