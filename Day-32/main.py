import datetime as dt
import random
from smtplib import *


now = dt.datetime.now()
weekday = now.weekday()

my_email = "firaforpython@gmail.com"
password = "odsfplyzjibggmof"

if weekday == 6:
    with open("quotes.txt", mode="r") as data_file:
        quote = data_file.readlines()
        quote_of_the_day = random.choice(quote)

    print(quote_of_the_day)

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="firaolanbessa170@gmail.com",
            msg=f"Subject:Quote Of The Day\n\n {quote_of_the_day}"
        )


# import datetime as dt
#
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=2001, month=10, day=23)
# print(date_of_birth)