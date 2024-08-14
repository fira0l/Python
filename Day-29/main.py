from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

lock_logo = PhotoImage(file="logo.png")
canvas = Canvas()
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1,row=0)


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

email_input = Entry()
email_input.config(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry()
password_input.config(width=21)
password_input.grid(column=1, row=3)

# Button

generate_button = Button(text="Generate Password")
generate_button.config(width=14)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add")
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
