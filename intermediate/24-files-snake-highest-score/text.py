# Com este formato não precisa do file.close()
# with open("text.txt") as file:
#     content = file.read()
#     print(content)

with open("text_test.txt", mode="a+") as file:
    file.write("\nnew text test")
    print(file.read())

# file = open("text.txt")
# content = file.read()
# file.close()
# print(content)
