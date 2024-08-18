##################### Extra Hard Starting Project ######################

from smtplib import *
import datetime as dt
import random
import pandas as pd


files_name = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
my_email = "youremail@gmail.com"
my_password = "Your app password"


# 1. Update the birthdays.csv
birth_day = pd.read_csv("birthdays.csv")
birth_day_dict = birth_day.to_dict(orient="records")

today = dt.datetime.now()
today_weekday = today.weekday()

name = ""
receiver_mail = ""

it_is_birthday = False

# print(today_weekday)
# 2. Check if today matches a birthday in the birthdays.csv

for date_of_birth in birth_day_dict:
    if today.day == date_of_birth["day"] and today.month == date_of_birth["month"]:
        name = date_of_birth["name"]
        receiver_mail = date_of_birth["email"]
        it_is_birthday = True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if it_is_birthday:
    letter = random.choice(files_name)
    print(letter)
    with open(file=f"letter_templates/{letter}", mode="r") as letter:
        content = letter.read()
        content = content.replace("[NAME]", name)
        print(content)

    with SMTP("smtp.gmail.com") as smtp:
        smtp.starttls()
        smtp.login(user=my_email, password=my_password)
        smtp.sendmail(to_addrs=receiver_mail, from_addr=my_email, msg=f"Subject: Wishing Happy Birthday\n\n{content}")


# 4. Send the letter generated in step 3 to that person's email address.




