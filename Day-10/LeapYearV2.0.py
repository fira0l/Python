def is_leap(year):
    if year % 4==0:
        if year%100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
def days_in_month(the_year,the_month):
    if month > 12 or month <1:
        return "Invalid Month"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(the_year) and month == 2:
        return 29
    month = month_days[int(the_month)-1]
    return month
    

year = int(input("Enter a Year: "))
month = int(input("Enter a month: "))
days = days_in_month(year,month)
print(days)