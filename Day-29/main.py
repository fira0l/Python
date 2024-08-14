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


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
window.mainloop()
