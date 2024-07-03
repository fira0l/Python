print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

drxn = input("You are at a cross road. Where Do u want to go? Type \"left\" or \"right\" \n").lower()

if drxn == "left":
    choice2 = input("You have come to lake Swim or Wait for a boat \n").lower()
    if(choice2 == "wait"):
        doors = input("You Have Survived to the island safely and know u see three doors red, blue and yellow. Which Door do u choose?").lower()
        if(doors == "red"):
            print("You are Burned by a fire wrong choice my friend!!! 🔥🔥🔥👨‍🚒")
        elif (doors == "yellow"):
            print("Congratulation, YOU HAVE FOUND THE TREASURE WELL DONE U HAVE LUCK IN CHOICES!!! 🪙🪙🪙")
        else:
            print("Dude U have think of ur choice no play the game again!!! 😞😞😒")
    else:
        print("Game Over, U have been eaten by Sharks and i Hope u choose wisely next time!!!🦈")
else:
    print("Game Over,U fell into a pit full of snakes , TRY AGAIN!!! 👿🐍")
    
