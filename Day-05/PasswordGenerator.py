banner = """
######                                                       #####                                                         
#     #   ##    ####   ####  #    #  ####  #####  #####     #     # ###### #    # ###### #####    ##   #####  ####  #####  
#     #  #  #  #      #      #    # #    # #    # #    #    #       #      ##   # #      #    #  #  #    #   #    # #    # 
######  #    #  ####   ####  #    # #    # #    # #    #    #  #### #####  # #  # #####  #    # #    #   #   #    # #    # 
#       ######      #      # # ## # #    # #####  #    #    #     # #      #  # # #      #####  ######   #   #    # #####  
#       #    # #    # #    # ##  ## #    # #   #  #    #    #     # #      #   ## #      #   #  #    #   #   #    # #   #  
#       #    #  ####   ####  #    #  ####  #    # #####      #####  ###### #    # ###### #    # #    #   #    ####  #    # 

"""
print(banner)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
randomInteger = random.randint(0,int(nr_letters)-1)
randomSymbol = random.randint(0,int(nr_symbols)-1)
randomNumbers = random.randint(0,int(nr_numbers)-1)


for passindex in range(0,int(nr_letters)):
    password.insert(randomInteger,letters[random.randint(0,len(letters)-1)])
for symbol in range(0,int(nr_symbols)):
    # password[randomInteger] = symbols[random.randint(0,len(symbols)-1)]
    password.insert(randomInteger,symbols[random.randint(0,len(symbols)-1)])
    password.pop()
for number in range(0,int(nr_numbers)):
    # password[randomInteger] = numbers[random.randint(0,len(numbers)-1)]
    password.insert(randomInteger,numbers[random.randint(0,len(numbers)-1)])
    password.pop()

print(print(f"You Generated Password is: \n"))
for passitem in password:
    print(passitem,end="")
print("\n")
print("============"*5)
# print(password)    