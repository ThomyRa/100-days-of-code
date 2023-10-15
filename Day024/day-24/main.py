absolute_path = "/home/thomy/Trainning/100-days-of-code/Day024/day-24/new_file.txt"
# relative_path = "../../../../../" + absolute_path
with open(absolute_path) as file:
    contents = file.read()
    print(contents)

# with open("new_file.txt", mode="w", encoding="utf8") as file:
#     file.write("This is a new text")