from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email_username = email_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: \nEmail: {email_username}"
                           f"\nPassword: {password} \nIs it ok to save?")

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!!!", message="You Have left some Fields blank fill them first")
    elif is_ok:
        with open("data.txt", mode="a") as data:
            data.writelines(f"{website} | {email_username} | {password}\n")
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)

        email_input.insert(0, "example@gmail.com")


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

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
