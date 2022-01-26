from os import name


list_of_names = ["Adeola", "Damilola", "Judith", "Helen"]

for i in range(len(list_of_names)):
    # if(len(list_of_names[i]) == 6):
    #     print(list_of_names[i])
    if(list_of_names[i].__contains__("a")):
        print(list_of_names[i])