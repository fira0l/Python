# from smtplib import *
#
# my_email = "firaforpython@gmail.com"
# password = "YourPassword"
#
# with SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="firaolanbessa170@gmail.com",
#         msg="Subject:Trial Test for the python program\n\n Hello, This is a body of the email"
#     )


import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
print(day_of_the_week)

date_of_birth = dt.datetime(year=2001, month=10, day=23)
print(date_of_birth)