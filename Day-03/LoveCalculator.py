print("Welcome to Love Calculator!")

name1 = input("What is Your Name? \n")
name2 = input("What is Your Lovers Name \n")

namea = name1.lower()
nameb = name2.lower()

names = namea+nameb

no_of_T = names.count("t")
no_of_R = names.count("r")
no_of_U = names.count("u")
no_of_E = names.count("e")
no_of_L=names.count("l")
no_of_O = names.count("o")
no_of_V = names.count("v")

TRUE = no_of_T + no_of_R + no_of_U + no_of_E
LOVE = no_of_L + no_of_O + no_of_V + no_of_E

perc = str(TRUE) + str(LOVE)
percent= int(perc)

if percent <10 or percent>90:
    print(f"Your score is {percent}, You Go together like coke and Mentos ❤️😍")   
elif percent >=40 and percent <=50:
    print(f"Your score is {percent}, You are alright Together 😘")
else:
    print(f"Your score is {percent} 💕💖")
