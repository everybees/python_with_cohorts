name = "Johnnie".upper()
last_name = "Doe".upper()
age = 47
s_o_o = "Lagos".upper()

for i in range(0, len(name), 2):
    print(name[i],age//10, sep = "", end="")
print()


for i in range(0, len(s_o_o),2):
    print(s_o_o[i], last_name, sep="", end="")
print()

for i in range(len(name)):
    print(name[i], end="-")
for i in range(len(last_name)):
    if(i != len(last_name)-1):
        print(last_name[i], end="-")
    else: print(last_name[i], end="")
print()