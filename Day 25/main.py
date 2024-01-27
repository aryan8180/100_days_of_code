# # with open("Day 25/weather_data.csv") as file:
# #     contents = file.readlines()
# #     print(contents)

# # import csv

# # with open("Day 25/weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# import pandas

# data = pandas.read_csv("Day 25/weather_data.csv")

# temp_list = data["temp"].to_list()
# temp_total = data["temp"].__len__()
# temp_maxi = data["temp"].max()

# sum = 0
# for t in temp_list:
#     sum += t
# avg = sum/temp_total

# # print(f"The average temperature off the given range of temperature is {avg}")
# # print(f"The maximum temperature is {temp_maxi}")

# # print(data["condition"])
# # print(data.day)

# # monday_temperature = data[data.day == "Monday"]
# # to_farhen = (int(monday_temperature.temp) * 9/5) + 32
# # print(monday_temperature.temp)
# # print(to_farhen)

# # Creating a DataFrame from scratch
# data_dict = {
#     "student" : ["Aryan","Happy","Jarvo"],
#     "scores" : [96,79,86]
# }

# data_scores = pandas.DataFrame(data_dict)
# print(data_scores)
# data_scores.to_csv("new.csv")

import pandas



data_orignal = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data_orignal[data_orignal["Primary Fur Color"] == "Gray"])

black_squirrels = len(data_orignal[data_orignal["Primary Fur Color"] == "Black"])

cinnamon_squirrels = len(data_orignal[data_orignal["Primary Fur Color"] == "Cinnamon"])

squirrel_count = {
    "Fur Color" : ["Grey","Cinimon","Black"],
    "count" : [gray_squirrels,cinnamon_squirrels,black_squirrels]
}

data = pandas.DataFrame(squirrel_count)
print(data)


