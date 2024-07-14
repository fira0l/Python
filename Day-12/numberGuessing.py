import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


NUMBER = random.randint(1,101)
# print(NUMBER)
# def validator(number):

end_of_game = False

def check_difficulty(difficulty):
    """This function checks user insertedthe difficulty and sets the number of chances based on the difficulty"""
    counter = 0
    if difficulty == 'easy':
        counter = 10
        return counter
    elif difficulty == 'hard':
        counter = 5
        return counter
    else:
        return "You Have Inserted A wrong Difficulty!!!"

number_of_chances = int(check_difficulty(difficulty))
                
while not end_of_game and number_of_chances != 0:
    user_input = int(input("Guess A Number: "))
    # counter = check_difficulty(difficulty)
    if user_input != NUMBER and number_of_chances != 0:
        if user_input > NUMBER:
            print("Too HIGH") 
        elif user_input < NUMBER:
            print("Too LOW")
        number_of_chances = number_of_chances - 1
        print(f"You Have Left with {number_of_chances} Chances")
    elif user_input == NUMBER:
        print("You WON!!!")
        end_of_game = True
    elif number_of_chances == 0:
        print("You Have Run Out of Chances!!!")
        end_of_game = True
    
    
    
