import csv
import pandas


# with open("weather_data.csv") as file:
#     # weather = file.readlines()
#     # print(weather)
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


data = pandas.read_csv('weather_data.csv')
print(data)
print(data['temp'])
data_dict = data.to_dict()
print(data_dict)
data_temp = data["temp"].tolist()
print(data_temp)
no_of_days = len(data_temp)
avg = sum(data_temp)/len(data_temp)
print(avg)
print(data["temp"].mean())
print(data["temp"].max())
print(data.condition)
print(data["condition"])
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp
monday_temp_f = monday_temp * 9/5 + 32
print(f"temperature in f of monday: {monday_temp_f}")


data_dict_1 = {
    "students": ["Jack", "Jill", "John"],
    "scores": [81, 24, 53],
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_file.txt")