import sys

name = 'IbiDapo Abdulazeez'


name_capitalize = name.capitalize()
name_lowercase = name.lower()

# print(name)
# print(name_lowercase)
# print(name_capitalize)


list_of_names = ['Helen', 'Paul', 'Joe', 'Rogen', 'Motunrayo', 'David', 'Johnson', 'Adeola Esther']
maximum = len(list_of_names[0])
minimum = sys.maxsize
for i in range(len(list_of_names)):
    length = len(list_of_names[i])
    if maximum < length:
        maximum = length
        value = list_of_names[i]
    if minimum > length:
        minimum = length
        val = list_of_names[i]
print(value)
print('The longest name is', maximum)

print(val)
print('The shortest name is ', minimum)

for i in range(len(list_of_names)):
    # print(list_of_names[i], len(list_of_names[i]))
    if len(list_of_names[i]) == 5:
        print(list_of_names[i])

for i in range(len(list_of_names)):
    if list_of_names[i].__contains__('gen'):
        print(list_of_names[i])


