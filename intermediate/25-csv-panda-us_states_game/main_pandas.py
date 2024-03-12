import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240307.csv")

data_fur = data["Primary Fur Color"]
data_fur.value_counts().to_csv("squirrel_count.csv")

# OR (after load de dataframe in data)

count_gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
count_red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

print(count_gray_squirrel)
print(count_red_squirrel)
print(count_black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray_squirrel, count_red_squirrel, count_black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count2.csv")
