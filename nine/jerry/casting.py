first_name = "Johnnie"
last_name = "Doe"
age = 47
state_of_origin = "Lagos"
for i in range(0, len(first_name), 2):
    print(first_name[i].upper(), age // 10, sep="", end="")

print()

for i in range(0, len(state_of_origin), 2):
    print(state_of_origin[i].upper(), sep=last_name.upper(), end=last_name.upper())

print()

for i in range(0, len(first_name)):
    print(first_name[i].upper(), end="-")
for i in range(0, len(last_name)):
    print(last_name[i].upper(), end="-") \
        if last_name[i].upper() != last_name[len(last_name)-1].upper() else print(last_name[i].upper(), end="")

