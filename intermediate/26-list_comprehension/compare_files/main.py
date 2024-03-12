import pandas as pd

data1 = pd.read_csv('file1.txt', header=None)
data2 = pd.read_csv('file2.txt', header=None)

data1.columns = ["a"]
data2.columns = ["a"]

list1 = data1["a"].to_list()
list2 = data2["a"].to_list()

intersection = [e for e in list1 if e in list2]

print(list1)
print(list2)
print(intersection)
