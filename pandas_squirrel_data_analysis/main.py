import csv
import pandas

#data = pandas.read_csv("weather_data.csv")
#data_dict = data.to_dict()

#Turns the series into a python list
#templist = data["temp"].to_list()

#print(data["temp"].mean())

#Bringing in the data from the squirrel_data csv file.
data = pandas.read_csv("squirrel_data.csv")
#Focusing on the primary fur color column and digging out the number of squirrels by color
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Grey"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

#Making a dictionary out of the squirrels and their fur colors
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]

}

#Turning the above into a dataframe
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")
