import tkinter


#create new window using tkinter
window = tkinter.Tk()
# set min size of window
window.minsize(width=100, height=80)
# set padding
window.config(padx=10, pady=10)
# create labels
window.title(string="Miles to Km converter")
label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)
label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)
label4 = tkinter.Label()
label4.grid(column=1, row=1)

# function to calculate miles to km
def calc_km():
    miles = float(value.get())
    km = miles * 1.609344
    label4.config(text=f"{km}")

# create an entry function
value = tkinter.Entry(width=10)
value.grid(column=1, row=0)
button = tkinter.Button(text="Calculate", command=calc_km)
button.grid(column=1, row=2)
window.mainloop()