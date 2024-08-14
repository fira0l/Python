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
canvas.pack()


window.mainloop()
