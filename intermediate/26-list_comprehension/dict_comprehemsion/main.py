import pandas

str = "What is the airspeed velocity of an Unladen Swallow?"
str_list = str.split()
str_dict = {word: len(word) for word in str_list}

print(str_dict)
