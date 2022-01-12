# Write a program that prints 
first_name = "Johnnie"
last_name = "Doe"
age = 47
s_o_o = "Lagos"

for i in range(0, len(first_name), 2):
    print(first_name[i].upper(), age // 10, sep=" ", end=" ")
print()

for i in range(0, len(s_o_o), 2):
    print(s_o_o[i].upper(), last_name, sep=" ", end=" ")
print()

concat = first_name + last_name

for i in range(0, len(concat)):
    print(concat[i].upper(), sep="-", end="-")

