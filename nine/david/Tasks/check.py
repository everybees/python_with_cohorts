name = "dAvId"
name_capitalize = name.capitalize()
name_lower = name.lower()
name_with_white_space = "            David        "
name_lstripped = name_with_white_space.strip()
name_rstripped = name_with_white_space.strip()
swapped = name.swapcase()


# print(name_lstripped)
# print(name_rstripped)
# print(swapped)
# print(name)
# print(name_lower)
# print(name_capitalize)

list_of_names = ["Hellen", "David", "Joe", "Rogen", "Motunrayo", "Johnson", "Adeola Esther", "Mofobi", "jim Doe"]

# longest = max(list_of_names, key=len)
# shortest = min(list_of_names, key=len)
# print(longest)
# print(shortest)

# counter = 1
# for each in list_of_names:
#     if len(each) > counter:
#         counter = len(each)
#         result = each

# print(result)

# maximum = 0
# for i in range(len(list_of_names)):
#     length = len(list_of_names[i])
#     if maximum < length:
#         maximum = length
#         value = list_of_names[i]

# print("Longest Name = ", value)
# print("Number = ", maximum)

# minimum = 1000
# for i in range(len(list_of_names)):
#     length = len(list_of_names[i])
#     if minimum > length:
#         minimum = length
#         value = list_of_names[i]

# print("Shortest Name = ", value)
# print("Number = ", minimum)

# printing smallest names
# smallest = 5
# for i in list_of_names:
#     if len(i) == smallest:
#         smallest = len(i)
#         result = i
#         print(result)


# # search if list contains some strings
# for i in list_of_names:
#     if i.__contains__("gen"):
#         print(i)


class_a = ["Hellen", "David", "Joe", "Rogen", "Motunrayo"]
class_b = ["Johnson", "Adeola", "Mofobi", "jim Doe"]



longest = 0
shortest = 0
for i in range(len(class_a)):
    lenght = len(class_a[i])
    if longest < lenght:
        longest = lenght
        value = class_a[i]
    else:
        if i in range(len(class_b)):
            lenght = len(class_b[i])
            if shortest < lenght:
                shortest = lenght
                value1 = class_b[i]

print("Class A longest name = ", value)
print("Class B longest name = ", value1)

if value < value1:
    print("Class A has longer name than Class B")
else:
    print("Class B has longer name than Class A")

# classes = [class_a, class_b]

# for i in range(len(classes)):
#     for j in range(len(classes[i])):
#         # print(classes[i][j])
#         if i > j:
#             print(i)
# if i < j:
#         print(j)