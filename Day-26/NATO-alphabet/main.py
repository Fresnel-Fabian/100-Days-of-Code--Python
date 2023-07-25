# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

def generate_nato_phonetics():
    try:
        word = input("Enter the word: ").upper()
        decoded_word = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please")
        generate_nato_phonetics()
    else:
        print(decoded_word)


generate_nato_phonetics()