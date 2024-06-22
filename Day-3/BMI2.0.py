height = float(input("enter Your Height in m: "))
weight = float(input("enter Your Weight in kg: "))


bmi=0

bmi = round(weight/height**2)

if(bmi<18.5):
    print(f"Your bodymass Index is : {bmi},You are Underweight ")
elif(bmi<25):
    print(f"Your bodymass Index is : {bmi},You are Normal Weight ")
elif(bmi<30):
    print(f"Your bodymass Index is : {bmi},You are overweight")
elif(bmi<35):
    print(f"Your bodymass Index is : {bmi}, you are Obese")
else:
    print(f"Your bodymass Index is : {bmi},You are Clinically Obesse")
