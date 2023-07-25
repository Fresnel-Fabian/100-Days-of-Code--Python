# TODO: Create a letter using starting_letter.txt
with open("Input/Names/invited_names.txt") as file:
    invited_names = file.readlines()
    print(invited_names)

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()
    print(letter)
text = "[name]"
for names in invited_names:
    name = names.strip("\n")
    print(name)
    new_letter = letter[0].replace(text, name)
    text = name
    letter[0] = new_letter
    print(letter)

    # Replace and save the letters
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
        for line in letter:
            file.write(line)

            