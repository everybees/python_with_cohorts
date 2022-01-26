# Author = Joshua

first_name = 'Johnnie'
lastname = 'Doe'
age = 47
state_of_origin = 'Lagos'

for i in range(0, len(first_name), 2):
    print(first_name[i].upper(), age // 10, sep="", end="")
print("\n")
for i in range(0, len(state_of_origin), 2):
    print(state_of_origin[i].upper() + lastname.upper(), end="")
print("\n")
for i in first_name:
    print(i.upper() + "-", end="")
for i in lastname:
    print(i.upper() + "-", end="")
