from arts import logo,vs
from Dictionary import data
import random
import os

def clear():
    os.system("cls")

def format_data(account):
    """Takes the account data and returns the Printanble Format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess,a_followers,b_followers):
    """Take the users guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
#Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
#make the game repeatable
while game_should_continue:
    # Making account at position B become the next account at position A

    
    #Generate A Random Account From the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    #Format the Account into Printable Format

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask User for a guess
    guess = input("Who has more Followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    ##get follower count of eacj account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ##use if statement to check if usesr is correct 
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    
    #clear the screen between Rounds
    clear()
    print(logo)
    #give feedback on their progress
    #score keeping
    if is_correct:
        score += 1
        print(f"You are Right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, That is Wrong. Final Score: {score}.")