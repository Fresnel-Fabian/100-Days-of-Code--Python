# try:
#     file = open(file="file.txt")
#     dict_a = {"key": "value"}
#     print(dict_a["key"])
# except FileNotFoundError as error_message:
#     print(error_message)
#     file = open(file="file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     f = file.read()
#     print(f)
# finally:
#     file.close()
#     print("File closed")
#
# height = float(input("Height:"))
# weight = float(input("Weight:"))
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
# bmi = weight/height**2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + "pie")
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        total_likes += 0
print(total_likes)
