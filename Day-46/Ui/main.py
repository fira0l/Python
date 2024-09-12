from tkinter import *

image = "./spotifylogo.png"

def someFunction():
    user_date = userinput.get()
    return user_date


window = Tk()
window.title("Spotify Billboard Playlist Creator")
window.config(pady=20,padx=20)

logo = PhotoImage(file=image)
canvas = Canvas()
canvas.config(width=768, height=231)
canvas.create_image((384,115),image=logo)
canvas.grid(column=0, row=0)


label = Label()
label.config(text="SPOTIFY BILLBOARD \nPLAYLIST CREATOR".upper(), font=("Helvetica", 30, "bold"), padx=20, pady=20)
label.grid(column=0, row=1)

inputlabel = Label()
inputlabel.config(text="Date", width=20)
inputlabel.grid(column=0, row=2)

userinput = Entry()
userinput.insert(0, "YYYY-MM-DD")
userinput.grid(column=0,row=2,columnspan=2)


button = Button()
button.config(text="Add To Playlist", command=someFunction)
button.grid(column=0, row=3)


window.mainloop()
