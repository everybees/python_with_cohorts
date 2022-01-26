first_name = "Johnnie"
last_name = "Doe"
age = 47
state_of_origin = "Lagos"
for i in range(0, len(first_name), 2):
    print(first_name[i].upper(), age // 10, sep="", end="")
print()
for i in range(0, len(state_of_origin), 2):
    print(state_of_origin[i].upper(), last_name.upper(), sep="", end="")
print()
for i in range(0, len(first_name)):
    print(first_name[i].upper(), "-", sep=" ", end="")
for i in range(0, len(last_name)):
    #git print(last_name[i].upper(), "-", sep=" ", end="")
    if i == len(last_name) - 1:
        print(last_name[i].upper())
    else:
        print(last_name[i].upper(), "-", end="")
