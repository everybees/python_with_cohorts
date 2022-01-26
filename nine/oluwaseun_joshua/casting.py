


first_name= "Johnnie"
last_name = "Doe"
age=47
state= "Lagos"

 
for i in range(0, len(first_name),2):
    print(first_name[i].upper(),age//10, sep="",end="")

print()

for i in range(0,len(state),2):
    print(state[i].upper(),last_name.upper()*1,sep="", end= "")

print()

full_name=str(first_name + last_name)

for i in range(0,len(full_name)):
    if i == len(full_name)-1:
        print(full_name[i].upper())
    else:
        print(full_name[i].upper(),end="-")
    

