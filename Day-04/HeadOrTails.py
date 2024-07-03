import random

toss = random.randint(0,1)

user = input("Enter Head or Tail ").lower()


if toss == 0:
        print("Tails")
        if user == "tail":
            print("You won!!!🎉")
        else:
            print("U lost!!!")
else:
        print("Heads")
        if(user=="head"):
            print("You Have won!!!🎉")
        else:
            print("You Have Lost!!!")