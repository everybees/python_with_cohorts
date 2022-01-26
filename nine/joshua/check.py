# Author: Joshua
# Title : Various tricks at play

# name = "JoSHua"
# name_with_white_space = "     sofowora"
# name_capitalize = name.capitalize()
# name_lower = name.lower()
# name_lstriped = name_with_white_space.lstrip()
# name_rstriped = name_with_white_space.rstrip("1")
# name_striped = name_with_white_space.strip()
# name_swaped = name.swapcase()
# # print(name)
# # print(name_lower)
# # print(name_capitalize)
# print(name_with_white_space)
# print(name_lstriped)
# print(name_rstriped)
# print(name_striped)
# print(name_swaped)

names = ["Samuel", "Chukwueze", "Makinwa", "macus", "john", "Local", "Legend"]

count = -1
maximum = 0
name = names[count]
minimum = 10000
# names_of_five = " "

while count < len(names)-1:
    count = count + 1
    if len(names[count]) > maximum:
        maximum = len(names[count])
        max_name = names[count]

    if len(names[count]) < minimum:
        minimum = len(names[count])
        name = names[count]

    if len(names[count]) == 5:
        names_of_five = names[count]
        print(names_of_five, sep="", end=" ")

    if names[count].__contains__("gen"):
        container = names[count]
        print(container, end=" ")

print()
print(maximum, max_name)

print(minimum, name)





