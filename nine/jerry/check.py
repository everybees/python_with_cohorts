# name = "ChiBuiFE"
# name_with_white_space = "     jerry"
#
# name_capitalize = name.capitalize()
# name_lower = name.lower()
# name_lstriped = name_with_white_space.lstrip()
# name_rstriped = name_with_white_space.rstrip()
#
# print(name)
# print(name_capitalize)
# print(name_lower)
# print(name_with_white_space)
# print(name_lstriped)
# print(name_rstriped)


# list_of_names = ["Helen", "Paul", "Joe", "Rogen", "Motunrayo", "David", "Johnson", "Adeola-Esther", "Mofobi", "John-Doe"]
# maximum = 0
# value = "A"
# index = 0
#
# for i in range(len(list_of_names)):
#     length = len(list_of_names[i])
#     if maximum < length:
#         maximum = length
#         value = list_of_names[i]
#         index = i
#     if len(list_of_names[i]) == 5:
#         print(list_of_names[i], end=" ")
#         print(i)
#     if list_of_names[i].__contains__("gen"):
#         print(list_of_names[i])
# print(value)
# print(maximum, "letters")
# print("Index", index)
import sys

class_a = ["Helen", "Paul", "Joe", "Rogen", "Motunrayo"]
class_b = ["David", "Adeola-Esther", "Mofobi", "John-Doe", "Ai"]

# longest_in_a = max(class_a, key=len)
# longest_in_b = max(class_b, key=len)
#
# smallest_in_a = min(class_a, key=len)
# smallest_in_b = min(class_b, key=len)
#
# if len(longest_in_a) > len(longest_in_b): print("Class A has the longest name:", longest_in_a)
# elif len(longest_in_b) > len(longest_in_a): print("Class A has the longest name:", longest_in_b)
#
# if len(smallest_in_a) < len(smallest_in_b): print("Class A has the smallest name:", smallest_in_a)
# if len(smallest_in_b) < len(smallest_in_a): print("Class B has the smallest name:", smallest_in_b)



classes = class_a, class_b
maximum = 0
minimum = sys.maxsize
value = ""
value_ = ""
for i in range(len(classes)):
    for j in range(len(classes[i])):
        length = len(classes[i][j])
        if maximum < length:
            maximum = length
            value = classes[i][j]

        if minimum > length:
            minimum = length
            value_ = classes[i][j]

print(value, maximum)
print(value_, minimum)



