from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label

my_label = Label(text="I am A Label", font=("Ariel", 15, "italic"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()



window.mainloop()

 