banner = """

######                                                                 #####                                              
#     #  ####   ####  #    #    #####    ##   #####  ###### #####     #     #  ####  #  ####   ####   ####  #####   ####  
#     # #    # #    # #   #     #    #  #  #  #    # #      #    #    #       #    # # #      #      #    # #    # #      
######  #    # #      ####      #    # #    # #    # #####  #    #     #####  #      #  ####   ####  #    # #    #  ####  
#   #   #    # #      #  #      #####  ###### #####  #      #####           # #      #      #      # #    # #####       # 
#    #  #    # #    # #   #     #      #    # #      #      #   #     #     # #    # # #    # #    # #    # #   #  #    # 
#     #  ####   ####  #    #    #     0 #    # #      ###### #    #     #####   ####  #  ####   ####   ####  #    #  ####  
                                                                                                                          
"""
                                    
print(banner)

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Choice = int(input("What Do You Choose?\n0.For Rock\n1.for Paper\n2.For Scissors\nYour choice: "))

computers_choice = random.randint(0,2)

choiceList = [rock,paper,scissors]

if computers_choice == 0:
    print(f"Computers Choice:\n{choiceList[0]}")
    if(Choice == 0):
        print(f"Your Choice:\n{choiceList[0]} ")
        print("=========="*5)
        print("DRAW!!!")
    elif(Choice == 1):
        print(f"Your Choice:\n{choiceList[1]}")
        print("=========="*5)
        print("You WON")
    elif(Choice == 2):
        print(f"Your Choice:\n{choiceList[2]}")
        print("=========="*5)
        print("YOU LOST!!!")
    else:
        print("WRONG INPUT")
elif computers_choice == 1:
    print(f"Computer Choice:\n{choiceList[1]}")
    if(Choice == 0):
        print(f"Your Choice: \n{choiceList[0]}")
        print("=========="*5)
        print("You WON")
    elif(Choice == 1):
        print(f"Your Choice: \n{choiceList[1]}")
        print("=========="*5)
        print("IT IS DRAW")
    elif(Choice == 2):
        print(f"Your Choice: \n{choiceList[2]}")
        print("=========="*5)
        print("You LOST")
    else:
        print("Wrong INPUT")
elif computers_choice == 2:
    print(f"Computers Choice: \n{choiceList[2]}")
    if(Choice==0):
        print(f"Your Choice: \n{choiceList[0]}")
        print("=========="*5)
        print("You WON")
    elif(Choice == 1):
        print(f"Your Choice: \n{choiceList[1]}")
        print("=========="*5)
        print("You LOST")
    elif(Choice == 2):
        print(f"Your Choice: \n{choiceList[2]}")
        print("=========="*5)
        print("IT IS DRAW")
    else:
        print("WRONG INPUT")
else:
    print("Unknown Choice!!!")
    
     
