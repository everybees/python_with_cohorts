# name ='Increase'
# name_with_white_space = 'joseph'
# name_capitalize = name.capitalize()
# name_lower = name.lower()
# name_lstriped = name_with_white_space.lstrip()
# name_rstriped = name_with_white_space.rstrip()
# name_striped = name_with_white_space.strip() 

# print(name)
# print(name_lower)
# print(name_capitalize)
# print(name_lstriped)
# print(name_rstriped)
# print(name_striped)


list_of_name = ['Ademijuwonlo-Taiwo', 'Increase-lois','helen','rogen','favor',
                    'damilola','Adeola', 'Lotachi','Paul','Esther','Olabanji']
for name in range(len(list_of_name)):
    print(len(list_of_name[name]))
    # print(list_of_name[0])

maximum = len(list_of_name[name])
for name in range(len(list_of_name)):
    if len(list_of_name[name]) > maximum:
        maximum = len(list_of_name[name])
        maximum_name = list_of_name[name]    

print("The name with the longest length is:",maximum_name, 'with', maximum)
print(maximum_name)

minimum = len(list_of_name[name])
for name in range (len(list_of_name)):
    if len(list_of_name[name]) < minimum:
        minimum = len(list_of_name[name])
        minimum_name = list_of_name[name]
print("The name with the shortest length is:",minimum,'with', minimum_name)
print()

# Print names and their indexes that have a length of 5
for name in range(len(list_of_name)):
    if (len(list_of_name[name]) == 5):
        print(list_of_name[name],"is a 5-lettered name")
print()

for name in range(len(list_of_name)):
    if list_of_name[name].__contains__('gen'):
        print(list_of_name[name])