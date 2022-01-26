
list_of_names = ["Adeola", "Damilola", "Judith", "Helen"]
for i in range(len(list_of_names)):
    first_len = len(list_of_names[0])
    if len(list_of_names[i]) > first_len:
        largest_name = list_of_names[i]
        print(largest_name) 
    if len(list_of_names[i]) < first_len:
        shortest_name = list_of_names[i]
        print(shortest_name)    
print()                                                                                                                                          