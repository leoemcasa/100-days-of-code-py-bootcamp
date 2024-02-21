programming_dictionary = {
    "Bug": "An error in a program that prevents it from running as expected",
    "Function": "A piece of code that you can easily reuse",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of iterate"

print(programming_dictionary)

# create an empty dictionary.
emp_dic = {}

# wipe an dictionary
# programming_dictionary = {}
print(programming_dictionary)

programming_dictionary["Bug"] = "A problem in a program that prevents it from running as expected"

# Loop
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

print(programming_dictionary)
print("----------")

for key, value in programming_dictionary.items():
    print(key, value)
#    print(programming_dictionary[key])
