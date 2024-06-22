order = """
Welcome to Python pizza Deliveries!!!

=======================================================
"""
print(order)

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do You want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print(f"Your Final bill is: ${bill}")

#or The Following code Will also works The same way

"""

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do You want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 
if size == "S":
    bill+=15
    if add_pepperoni == "Y":
        bill+=2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill+=20
    if add_pepperoni == "Y":
        bill+=3
    if extra_cheese == "Y":
        bill += 1
elif size == "L" or "l":
    bill+=25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill +=1
else:
    print("You Have entered Wrong Input!!!")
print(f"Your Final Bill is: ${bill}")

"""

