from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_meter_result_label.config(text=f"{km}")
def km_to_miles():
    km = 0
    mile = km / 1.606


window = Tk()
window.title("Miles to Kilometer Distance Converter")
# window.minsize(width=500,height=300)
window.config(padx=20,pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)
# miles_label.grid(column=0, row=0)
# label.pack(side="left")


is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0,row=1)

# my_label = Label(text="Is Equal To")
# my_label.grid(column=0,row=150)
kilo_meter_result_label = Label(text="0")
kilo_meter_result_label.grid(column=1,row=1)

kilo_meter_label = Label(text="Km")
kilo_meter_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)

window.mainloop()