"""
Leap year Defination:
    on every year that is evenly divisible by 4
        except every year that is evenly divisible by 100
          unless the year is also evenly divisible by 400
"""

year = int(input("Which Year do You want to check? "))

if year%4 == 0:
    if year%100 == 0: 
        if year%400 == 0:
            print(f"The Year {year} is Leap Year")
        else:
            print(f"The Year {year} is not Leap Year")
    else:
        print(f"The Year {year} is Leap Year")
else:
    print(f"The Year {year} is not Leap Year")
    