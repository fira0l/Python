# #to do
# from arts import logo,vs
# from Dictionary import data
# import random
# import os
# #logo
# print(logo)
# #Landing Page
# print("""WHO HAS MORE FOLLOWERS ON INSTAGRAM?
# A frustratingly addictive game of higher or lower using INSTAGRAM FOLLOWS.
# The data is based on IDEAL INSTAGRAM FOLLOWS.
# """)
# #Handling User Input
# #creating a Function That Handles the comparision of values
# #Looping
# #game Status

# counter = 0

# ## Courses Comments
# def clear():
#     os.system("cls")
# # Generate a random account from the game data
# def Account(dt,choice):
#     """This Function is Used To Retrive and Assign Values of Respective Dictionary Values"""
#     account = random.choice(dt)
# # print(account)
# # Format account data into printable format.
#     name = account["name"]
#     follower_count = int(account["follower_count"])
#     description = account["description"]
#     country = account["country"]
    
#     print(f"{choice} = {name}, {country}")
#     print(description)
#     return follower_count
# a = Account(dt=data,choice="A")
# print(vs)
# b = Account(dt=data,choice="B")
# # Ask user for a guess.
# Users_input = input("Guess Which Of the Two Has More Followers: ").lower()
# # Check if user is correct.

# FollowerA = int(a)
# FollowerB = int(b)

# if Users_input == "a" or Users_input == "b":
#     if FollowerA > FollowerB or FollowerA == FollowerB:
#         counter += 1
#         a = b
#         b = Account(dt=data,choice="B")
#     elif FollowerA<FollowerB:
#         print("Game Over !!!")
#         # clear()
        
#     ## Get follower count.

# ## If Statement

# # Feedback.

# # Score Keeping.

# # Make game repeatable.

# # Make B become the next A.

# # Add art.

# # Clear screen between rounds.

