
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You Got it")
# my_function()

# from random import randint
# dice_imgs = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])


year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a Millenial.")
elif year >= 1994:
    print("You are a Gen Z.")
