# FileNotFoundError
# with open("non_existent_file.txt") as file:
#     file.read()
try:
    file = open("nonexistent_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError as e:
    file = open("nonexistent_file.txt", "w")
    file.write("criado")
    print(f"Nonexistent {e.filename} criado")
except KeyError as e:
    print(f"Nonexistent {e} key")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file closed")
    raise ValueError("',' not allowed")

# KeyError
# a_dict = {"key": "value"}
# a_value = a_dict["non_existent_key"]

# IndexError
# a_list = ["Apple", "Banana", "Pear"]
# fruit = a_list[3]

# TypeError
# text = "abc"
# print(text + 5)
