with open("new_file.txt", mode="w") as file:
    file.write("hello")

with open("new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="a") as file:
    file.write("\nHi")