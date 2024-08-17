from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")

    password_input.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get().lower()
    email_username = email_input.get()
    password = password_input.get()
    new_data = {website:{
        "email":email_username,
        "password":password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!!!", message="You Have left some Fields blank fill them first")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old Data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Writing to the file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SEARCH SETUP ------------------------------- #

def search():
    users_search = website_input.get().lower()
    with open("data.json", "r") as datafile:
        data = json.load(datafile)
        try:
            email = data[users_search]["email"]
            password1 = data[users_search]["password"]
        except KeyError:
            messagebox.showinfo(title="Website Not Found", message="Website is not registered. register it first.")
        else:
            messagebox.showinfo("Found Website",f"email: {email}\npassword: {password1}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

lock_logo = PhotoImage(file="logo.png")
canvas = Canvas()
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)


# Label

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Input

website_input = Entry()
website_input.config(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry()
email_input.config(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@gmail.com")

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

# Button

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", command=save)
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search,width=14)
search_button.grid(row=1,column=3)
window.mainloop()
