# Author: Joshua
# Title : looping through array
variable = [["Bananas", "Oranges", "Mangoes"], ["Bread", "Eggs", "Tomatoes"], ["Rice", "Beans", "Yams"]]
for main_number in range(len(variable)):
    print()
    for sub_number in range(0, 3):
        print(variable[main_number][sub_number], "\t\t  ", end="")

print("\n", sep="")
for first_count in range(len(variable)):
    for second_number in range(0, 3):
        print(variable[first_count][second_number], "    [{}]-[{}]".format(first_count, second_number))

print("\n", sep="")
for first_count in range(len(variable)):
    for second_number in range(0, 3):
        print(variable[second_number][first_count], "    [{}]-[{}]".format(second_number,first_count))

print("\n", sep="")
for first_count in range(len(variable)-1, -1, -1):
    for second_number in range(0, 3):
        print(variable[second_number][first_count], "    [{}]-[{}]".format(second_number,first_count))

print("\n", sep="")
for first_count in range(len(variable)-1, -1, -1):
    for second_number in range(0, 3):
        print(variable[first_count][second_number], "    [{}]-[{}]".format(first_count, second_number))

print("\n", sep="")
for first_count in range(len(variable)-1, -1, -1):
    for second_number in range(2, -1, -1):
        print(variable[first_count][second_number], "    [{}]-[{}]".format(first_count, second_number))

print("\n", sep="")
for first_count in range(len(variable)-1, -1, -1):
    for second_number in range(2, -1, -1):
        print(variable[second_number][first_count], "    [{}]-[{}]".format(second_number, first_count))