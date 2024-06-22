Height = int(input("Enter Your Height (in cm) : "))
print("============="*5)

if Height >= 120:
    age = int(input("Enter Your Age: "))
    if age < 12:
        print("You have to pay $5 to Ride the Rollercoaster")
    elif age < 18:
        print("You have to pay $7 to Ride the Rollercoaster")
    else:
        print("You have to pay $12 to Ride the Rollercoaster")
else:
    print("You are not allowed to Ride the rollercoaster !!! GAIN SOME HEIGHT BUDDY")

print("============="*5)
