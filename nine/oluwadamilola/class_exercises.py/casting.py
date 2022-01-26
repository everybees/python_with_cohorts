first_name = "Johnnie"
second_name = "Doe"
age =  47
state_of_origin = "Lagos"

for i in range(0, len(first_name), 2):
    print(first_name[i].upper(), age//10, sep="", end="")
print()

for i in range(0, len(state_of_origin), 2):
    print(state_of_origin[i].upper(), second_name.upper(), sep="", end="")
print()

for i in range(0, len(first_name)):
    print(first_name[i].upper(), "-", end="")
for j in range (0, len(second_name)):
    if j == len(second_name) - 1:
        print(second_name[j].upper())
    else:
        print(second_name[j].upper(), "-", end="")
print()

full_name = first_name.upper() + second_name.upper()
for i in range (len(full_name)):
    if i == len(full_name) - 1:
        print(full_name[i])
    else:
        print (full_name[i], end="-")
print()