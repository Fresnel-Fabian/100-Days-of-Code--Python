# import pandas library
import pandas
# read csv file using pandas read_csv function to data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# select the Primary fur color column from data
fur_color = data["Primary Fur Color"]
# convert fur_color to list
fur_list = fur_color.to_list()
print(fur_list)
# using count functioon find the number of occurences of an element
gray = fur_list.count("Gray")
cinnamon = fur_list.count("Cinnamon")
black = fur_list.count("Black")
# create a dictionary fur_dict with the values
fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}
# creata a new pandas Dataframe with fur_dict
new_data = pandas.DataFrame(fur_dict)
print(new_data)