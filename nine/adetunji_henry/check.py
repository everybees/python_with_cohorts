# name = "Adetunji"
# name_with_white_space = "   Henry"
# name_capitalize = name.capitalize()
# # name_lower = name.lower()
# name_with_white_space.lstrip()
# name_striped = name_with_white_space
# name_lstriped = name_with_white_space.lstrip()
# name_rstriped = name_with_white_space.rstrip()
# name_swapped = name.swapcase()

# print(name)
# print(name_capitalize)
# print(name.lower())
# print(name_with_white_space)
# print(name_striped)
# print(name_lstriped)
# print(name_rstriped)
# print(name_swapped)
import sys

list_of_names = ["Helen", "Paul", "Joe", "Rogen", "Motunrayo", "David", "Johnson", "Adeola Esther", "Mofobi", "John-Doe"]
# there is a list called list_of_names

for i in range(len(list_of_names)):
    # if len(list_of_names[i]) == 5:
    if (list_of_names[i]).__contains__("gen"):
        print(True)
        # print(list_of_names[i])

#         length = len(list_of_names[i]) == 5
#         if maximum > length:
#             maximum = length
#             value = list_of_names[5]

# print(value)
# print(maximum)


for i in range(9):
    print(list_of_names[i], len(list_of_names[i]))
# the above "for loop" is meant to run through the list_of_names to determine which name has the highest letters

print(len(list_of_names[3]))
print(len(list_of_names[i]))
# i = 0
# while i < len(list_of_names):
#     print(list_of_names[i], len(list_of_names[i]))
#     i += 1
# the above "while loop" is meant to run thru the list_of_names to determine which name has the highest letters

#
# value = "a"
# maximum = 0
# for i in range(len(list_of_names)):
#     # if i == 0:
#         length = len(list_of_names[i])
#         if maximum < length:
#             maximum = length
#             value = list_of_names[i]

# print(value)
# print(maximum)


# if i > 0:
#     length = len(list_of_names[i])
#     if maximum < length:
#         maximum = length
#         value = list_of_names[i]

# value = "a"
# minimum = sys.maxsize
# for i in range(len(list_of_names)):
#     # if i == 0:
#         length = len(list_of_names[i])
#         if minimum > length:
#             minimum = length
#             value = list_of_names[i]
#
# print(value)
# print(minimum)
