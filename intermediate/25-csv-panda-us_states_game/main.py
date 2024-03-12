# import csv
#
# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     next(data, None)
#     temperatures = []
#     for e in data:
#         temperatures.append(int(e[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

tmp_list = data["temp"].to_list()
print(tmp_list)

print(sum(tmp_list) / len(tmp_list))

print(data["temp"].mean())

def avg_list(list):
    tot_sum = 0
    tot_e = len(list)
    for e in list:
        tot_sum += e

    return tot_sum/tot_e


print(avg_list(tmp_list))

print(data["temp"].max())
print(data[data["day"] == "Monday"])
print(data[data["temp"] == data["temp"].max()])
print("##############")
monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/ 5 + 32
print(monday_temp_f)

# Create Dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
