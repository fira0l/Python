from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("LangCard")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263,text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0)





window.mainloop()

