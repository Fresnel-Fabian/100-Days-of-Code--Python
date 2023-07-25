import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail: {email}\nPassword: {password}"
                                                              f"\nIs it ok to save?")
        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website}|{email}|{password}\n")
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
# window
window = tkinter.Tk()
window.title(string="Password Manager")
window.config(padx=50, pady=50, bg="white")
# convert logo to image that can be used in a canvas
logo_image = tkinter.PhotoImage(file="logo.png")
# canvas
canvas = tkinter.Canvas(height=200, width=189, bg="white", highlightthickness=0)
# insert image
canvas.create_image(100, 94, image=logo_image)
canvas.grid(row=0, column=1)
# Labels
website_label = tkinter.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)
# Entry's
website_entry = tkinter.Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "frenelfabian@gamil.com")
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)
# buttons
generate_password = tkinter.Button(width=13, text="Generate Password", bg="white", highlightthickness=0,
                                   command=generate_password)
generate_password.grid(row=3, column=2, columnspan=1)
add = tkinter.Button(width=36, text="Add", bg="white", highlightthickness=0, command=save)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()
