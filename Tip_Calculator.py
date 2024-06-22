print("Welcome To the tip CALCULATOR.")
total = float(input("What was the total bill? $"))
people = int(input("How many People to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))


tip = 0

if(percentage == 10):
    tip = (total/people)+(total/people)*0.1
    print(f"Each Person Should pay:${round(tip,1)}")
elif(percentage == 12):
    tip = (total/people)+(total/people)*0.12
    print(f"Each Person Should pay:${round(tip,1)}")
elif(percentage == 15):
    tip = (total/people)+(total/people)*0.15
    print(f"Each Person Should pay:${round(tip,1)}")
else:
    print("Wrong percentage!!!")



