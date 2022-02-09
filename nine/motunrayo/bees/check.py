from typing import List


list_of_names = ["Helen","Paul","Joe","Rogen","Motunrayo","David","Johnson","Adeola-Esther","Mofobi","John-joe"]
value = "a"
maximum = 0
for i in range(len(list_of_names)):
    length = len(list_of_names[i])
    if maximum < length:
        maximum = length 
        value = list_of_names[i]
print(value)
print(maximum)


value = "a"
minimum = 1000
for i in range(len(list_of_names)):
    length = len(list_of_names[i])
    if minimum > length:
        minimum = length
        value = list_of_names[i]
print(value)
print(minimum)

for i in range(len(list_of_names)):
   if  len(list_of_names[i])== 5:
       print(list_of_names[i])


for i in range(len(list_of_names)):
    if list_of_names[i].__contains__("gen"):
      print(list_of_names[i])
