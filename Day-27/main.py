from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label

my_label = Label(text="I am A Label", font=("Ariel", 25, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    inputed_text = input.get()
    my_label.config(text=f"{inputed_text}!!!")

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry: it is input

input = Entry()
input.pack()




window.mainloop()

 