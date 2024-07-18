
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You Got it")
# my_function()

#Reproducing Bugs 
# from random import randint
# dice_imgs = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])


# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a Millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")


# #Fix the errors
# age = int(input("How old are You? "))
# if age >18:
#     print(f"You can Drive at the age {age}")

# #print is Your Friend

# pages = 0
# word_per_page = 0 
# pages = int(input("NUmber of Pages: "))
# word_per_page = int(input("Number of Words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#use a debugger

def mutate(a_list):
    b_list =[]
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])