first_name = 'johnnie'
last_name = 'doe'
age = 47
s_o_o = 'lagos'

for i in range(0, len(first_name), 2):
    print(first_name[i].upper(), age // 10, sep="", end="")

print()

for j in range(0, len(s_o_o), 2):
    print(s_o_o[j].upper(), last_name.upper(), sep="", end="")
print()

full_name = first_name + last_name
for i in range(len(full_name)):
    if i == len(full_name) - 1:
        print(full_name[i].upper())
    else:
        print(full_name[i].upper(), end="-")
