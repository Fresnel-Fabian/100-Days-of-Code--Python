import pandas as pd


student_dict = {
    "student": ["Angels", "James", "lily"],
    "score": [56, 76, 98],
}
alphabets = ["a", "b", "c", "d", "e"]
new_alphabets = [letter + "a" for letter in alphabets]
new = {key: value for (key, value) in student_dict.items() if key == "student"}
print(new)
print(new_alphabets)
data = pd.DataFrame(student_dict)
print(data)
for (index, row) in data.iterrows():
    if row.student == "Angels":
        print(row.score)