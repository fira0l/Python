from tkinter import *
def button_clicked():
    inputed_text = input.get()
    my_label.config(text=f"{inputed_text}!!!")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)


# Label
my_label = Label(text="I am A Label", font=("Ariel", 25, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry: it is input
input = Entry()
print(input.get())
input.grid(column=3,row=2)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)



window.mainloop()

 