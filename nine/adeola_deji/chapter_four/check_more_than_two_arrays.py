array1 = ["Adeola", "Lo", "Helen", "Lekan", "Judith", "Increase", "Adeola-Esther"]
array2 = ["Jerry", "Shola", "Lota", "Damilola", "Motunrayo"]

my_list = [array1, array2]
first_len = len(my_list[0][0])
largest_name =""
smallest = my_list[0][0]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        maxi = 1000
        mini = 0
        if len(my_list[i][j]) > mini:
            largest_name = my_list[i][j]
            largest_index = j
        if len(my_list[i][j]) < maxi:
            smallest = my_list[i][j]
            smallest_index = j
    # print(largest_name)
    # print(smallest)
        
print(largest_index, largest_name) 
print(smallest_index, smallest) 

