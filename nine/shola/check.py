name = "SHoLa"
name_capitalize = name.capitalize()
name_lower = name.lower()
name_with_white_space = "   Azeez"
name_stripped = name_with_white_space.lstrip()
name.rstrip()
name.strip()
name_swapped = name.swapcase()
list_of_names = ['Helen', 'Paul', 'Joe', 'Rogen', 'Motunrayo', 'Agbabiaka', 'Mbadiwe-Ozumba', ]
# print(list_of_names[2])
# print(len(list_of_names[2]))
# print(len(list_of_names))
# print(name)
# print(name_capitalize)
# print(name_lower)
# print(name_stripped)
# print(name_swapped)

value = "a"
maximum = 0
for i in range(len(list_of_names)):
    length = len(list_of_names[i])
    if maximum < length:
        maximum = length
        value = list_of_names[i]

# print(value)
# print(maximum)

name_contains = list_of_names[i].__contains__('gen')
print(name_contains)

print(name[0])
