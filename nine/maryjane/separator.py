age=47
age= int (age)
firstName="Johnnie"
lastName="Doe"
fullName=firstName+" "+lastName
stateOfOrigin="Lagos"

print(firstName)
for i in firstName:
    print(i.upper(),age//10, sep="", end="")
print("")


for i in range(0,len(firstName),2) :
        print(firstName[i].upper(), age//10, sep="", end="")
# for i in stateOfOrigin:
#     print(i.upper(), lastName.upper(), sep="", end="")
print()
for i in firstName:
    print(i.upper(), "-", sep="", end="")
for i in lastName:
    print(i.upper(), "-", sep="", end="")

    # if(i==fullName[len(fullName)-1]):
    #     print(fullName[i].replace("-", ""), )

print()


for i in range(0,len(stateOfOrigin),2) :
        print(stateOfOrigin[i].upper(), lastName.upper(),sep="",  end="")
print(fullName)

