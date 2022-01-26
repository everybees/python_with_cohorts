first_name = "Johnnie"
last_name ="Doe"
age = 47
state_of_origin = "Lagos"

#J4H4N4E4
#LDOEGDOESDOE
#J-O-H-N-N-I-E-D-O-E


for i in range(0,len(first_name),2):
    print(first_name[i].upper(),age//10,sep="",end="")

print()
    
for i in range(0,len(state_of_origin),2):
            print(state_of_origin[i].upper(),last_name.upper(), sep="",end="")

print()

first_name = first_name.upper()
for i in range(0,len(first_name)):
    print(first_name[i],sep="",end="-")


last_name=last_name.upper()
for i in range(0,len(last_name)):
    if i == len(last_name) - 1:
        print(last_name[i])
    else:
        print(last_name[i], end="-")
    



# full_name =first_name.upper() + last_name.upper()
# for i  in range(len(full_name)):
#     if i == len(full_name) - 1:
#         print(full_name[i])
#     else:
#         print(full_name[i], end="-")

# print()