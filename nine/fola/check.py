

# name = "FoLa"
# name_with_white_space = "     sanni"
# name_with_white_lspace = "     sanni"
# name_with_white_rspace = "sanni     "

# # name_capitalize = name.capitalize()
# # name_lower = name.lower()

# name_stripped = name_with_white_space.strip()
# name_lstripped = name_with_white_space.lstrip()
# name_rstripped = name_with_white_space.rstrip()

# name_swapcase = name.swapcase() # changes any cases upper to lower
#
#
# # print(name)
# # print(name_lower)
# # print(name_capitalize)
#
# print(name_with_white_space)
# print(name_stripped)
# print(name_lstripped)
# print(name_rstripped)

# print(name_with_white_lspace)
# print(name_with_white_rspace)



list_of_names = ["Baba", "Kalu", "Audu", "Fola", "Stephen", "Bisi", "Johnson", "Agbabiaka", "Oluwadamilare", "Ademiju", "Rogen"]

# FIND NAME WITH THE HIGHEST NUMBER OF LETTERS AND DISPLAY HOW MANY IT IS

name = "a"
maximum = 0

for i in range(len(list_of_names)):
    length = len(list_of_names[i]) # The content at the 1st index, and henceforth!!!
    if maximum < length:
        maximum = length
        name = list_of_names[i]

print(name)
print(maximum)

print()

name = "i"
minimum = 1000

for i in range(len(list_of_names)):
    length = len(list_of_names[i]) # The content at the 1st index, and henceforth!!! should be called "length"
    if minimum > length:
        minimum = length
        name = list_of_names[i]

print(name)
print(minimum)

print()

for i in range(len(list_of_names)):
    if list_of_names[i].__contains__("ola"): # If the content at the 1st index, and henceforth, contains "ola"
        print(list_of_names[i])

print()

# PRINT NAMES AND THEIR INDEXES THAT HAVE 'x' LENGTH OF NUMBERS

for i in range(len(list_of_names)):
    if len(list_of_names[i]) == 7: # If the content at the 1st index, and henceforth, has the length of "x"
        print(list_of_names[i])
print()



class_a = ["Helen", "Motunrayo", "Paul", "Joe", "Rogen"]
class_b = ["David", "Johnson", "Esther", "Mofobi", "John"]

name_ = "a"
maximum = 0 # (or -sys.maxsize)
classes = [class_a, class_b]


for row in range(len(classes)):
    for column in range(len(classes[row])):
        length = len(classes[row][column]) # The content at the 1st index (row & column), and henceforth!!!
        if maximum < length:
            maximum = length
            name_ = classes[row][column]

print(name_, maximum)
print()

_name_ = "i"
minimum__ = 1000 # (or sys.maxsize)
classes_ = [class_a, class_b]

for row in range(len(classes_)):
    for column in range(len(classes_[row])):
        length = len(classes_[row][column]) # The content at the 1st index (row & column), and henceforth!!!
        if minimum__ > length:
            minimum__ = length
            _name_ = classes_[row][column]

print(_name_, minimum__)
print()

