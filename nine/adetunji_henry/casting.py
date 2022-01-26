first_name = "Johnnie"
last_name = "Doe"
age = 47
state_of_origin = "Lagos"


for i in range(0, len(first_name), 2):
    print(first_name[i].upper(), age//10, sep="", end="")
print ("\n")

for i in range(0, len(state_of_origin), 2):
    print(state_of_origin[i].upper(),last_name.upper(),sep="", end="")
print("\n")

full_name = first_name + last_name
# for i in range(len(full_name.upper())):
#      if i == len(full_name) - 1:
#          print(full_name[i].upper())
#      else:
#         print(full_name[i].upper(), end="-")

for i in range(len(first_name.upper()) + len(last_name.upper())):
    if i == len(full_name) - 1:
        print(full_name[i].upper())
    else:
        print(full_name[i].upper(), end="-")

