#to do
from arts import logo,vs
from Dictionary import data
import random
#logo
print(logo)
#Landing Page
print("""What gets Googled more?
A frustratingly addictive game of higher or lower using Google searches.
The data is based on global monthly searches.
""")
#Handling User Input
#creating a Function That Handles the comparision of values
#Looping
#game Status

## Courses Comments
# Generate a random account from the game data.
def Account(dt,choice):
    """This Function is Used To Retrive and Assign Values To Respective Dictionary Values"""
    account = random.choice(dt)
# print(account)
# Format account data into printable format.
    name = account["name"]
    follower_count = int(account["follower_count"])
    description = account["description"]
    country = account["country"]
    
    print(f"{choice} = {name}, {country}")
    print(description)
    
a = Account(dt=data,choice="A")
print(vs)
b = Account(dt=data,choice="B")



# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.