# import modules
import tkinter as tk
import pandas as pd
from random import choice

text = None
BACKGROUND_COLOR = "#B1DDC6"
# French words and their english translation
try:
    data = pd.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(filepath_or_buffer="data/french_words.csv")
finally:
    french_english = data.to_dict(orient="records")
    print(len(french_english))


# French translation with changes to the canvas
def french_word():
    # global variables
    global text, flip_timer
    # invalidate the flip timer
    window.after_cancel(flip_timer)
    # if the words in the french_english list runs out
    if not french_english:
        canvas.itemconfig(language_text, text="You", fill="black")
        canvas.itemconfig(word_text, text="Win", fill="black")
    else:
        text = choice(french_english)
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=text.get("French"), fill="black")
        canvas.itemconfig(canvas_image, image=card_front)
        flip_timer = window.after(3000, english_translation)


# English translation with changes to the canvas
def english_translation():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=text.get("English"), fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


# Remove the word because the user knows the word
def know():
    global french_english
    french_english.remove(text)
    new_data = pd.DataFrame(french_english)
    new_data.to_csv(path_or_buf="data/words_to_learn.csv", index=False)
    french_word()


# create window using Tk module
window = tk.Tk()
window.title(string="Flash Card")
# window.minsize(width=600, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# change card to english translation
flip_timer = window.after(3000, func=english_translation)
# load images using PhotoImage
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
# Create canvas
canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
# labels
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# button
right_button_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_button_image, highlightthickness=0, command=know)
right_button.grid(row=1, column=1)
wrong_button_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_button_image, highlightthickness=0, command=french_word)
wrong_button.grid(row=1, column=0)

french_word()

window.mainloop()