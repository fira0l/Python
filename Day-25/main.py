# # with open("./weather-data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# import csv
# with open("./weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather-data.csv")
# print(type(data))

# print(type(data["temp"]))

#DataFrame and Series in Pandas

# Data to Dictionary
data_dict = data.to_dict()
print(data_dict)

# Data series to list

temp_list = data["temp"].to_list()
summation = 0
average = 0
for item in temp_list:
    summation += item
    average = summation / len(temp_list)
print(f"the Average Temp is: {average}")
print(temp_list)

