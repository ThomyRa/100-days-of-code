#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def get_names(path):
    with open(path, "r", encoding="utf8") as f:
        contents = f.readlines()
    lines = []
    for line in contents:
        lines.append(line.strip("\n"))
    return lines


def replace_text(text_to_replace, list_of_people, path_file_being_replace):

    PATH_OUTPUT_LETTERS = "./Output/ReadyToSend/"

    with open(path_file_being_replace, "r", encoding="utf8") as file:
        starting_letter = file.read()

    for name in list_of_people:
        print(name)
        new_text = starting_letter.replace(text_to_replace, name)
        path_new_file = f"{PATH_OUTPUT_LETTERS}/letter_for_{name}.txt"

        with open(path_new_file, "w", encoding="utf8") as file:
            file.write(new_text)


NAMES_PATH = "./Input/Names/invited_names.txt"
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
names = get_names(NAMES_PATH)
print(names)

replace_text("[name]", names, STARTING_LETTER_PATH)

##################################################

# path = "./Input/Names/invited_names.txt"

# with open("./Input/Names/invited_names.txt", "r", encoding="utf8") as file:
#     names = file.readlines()


# print(names)
