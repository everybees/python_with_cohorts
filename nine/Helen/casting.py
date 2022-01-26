last_name = "Doe"
state_of_origin = "Lagos"
first_name = "Johnnie"
for i in range(0, len(state_of_origin), 2):
 print(state_of_origin[i].upper(),last_name.upper(), sep="", end="")
print()
# full_name = first_name + last_name

# for i in range(len(full_name)):
#     if i ==len(full_name)-1:
#         print(full_name[i].upper())
#     else:
#         print(full_name[i].upper(), sep = "", end="-")
