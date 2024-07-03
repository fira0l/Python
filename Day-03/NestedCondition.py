Height = int(input("Enter Your Height (in cm) : "))
print("============="*5)

bill = 0 

if Height >= 120:
    age = int(input("Enter Your Age: "))
    if age < 12:
        bill = 5
        print("Child Tickets are $5")
    elif age < 18:
        bill = 7
        print("Youth Tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be okay, have a free ride on us!!!")
    else:
        bill = 12
        print("Adult Tickets are $12")
    wants_photo = input("Do You want to a Photo Taken? Y or N.")
    if wants_photo == "Y" or "y":
        bill+=3

    print(f"The total amount to pay is : ${bill}")

else:
    print("You are not allowed to Ride the rollercoaster !!! GAIN SOME HEIGHT BUDDY")

print("============="*5)
