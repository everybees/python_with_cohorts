first_name = "Johnnie"
last_name = "Doe"
age = 47
state_of_origin = "Lagos"
# write a program that prints; J4H4N4E4
# LDOEGDOESDOE
# J-O-H-N-N-I-E-D-O-E

for i in range(0, len(first_name), 2):
     print(first_name[i].upper(), age//10, sep="", end="")
print(" ")

for i in range(0, len(state_of_origin), 2):
   print(state_of_origin[i].upper(), last_name.upper(), sep="", end="")

print(" ")

for i in range(len(first_name)+len(last_name)):
     if i == (len(first_name)+len(last_name) - 1):
          print(((first_name.upper())+(last_name.upper()))[i])
     else:
          print((first_name.upper()+last_name.upper())[i], end="-")
