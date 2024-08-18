from smtplib import *

my_email = "firaforpython@gmail.com"
password = "YourPassword"

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="firaolanbessa170@gmail.com",
        msg="Subject:Trial Test for the python program\n\n Hello, This is a body of the email"
    )
