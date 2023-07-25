import tkinter

window = tkinter.Tk()

window.title("First GUI Project")
window.minsize(width=600, height=300)
my_label = tkinter.Label(text="My first label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


def button_got_clicked():
    print("Button got clicked")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click me", command=button_got_clicked)
button.grid(column=1, row=1)
button1 = tkinter.Button(text="Button")
button1.grid(column=2, row=0)

window.mainloop()