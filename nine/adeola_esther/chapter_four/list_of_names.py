list_of_names=["Helen", "Paul", "Joe", "Rogen","Fola", "Ademijuwonlo", "Jibola","Increase", "Tolu","Motunrayo","Shola","Adeola-Esther"]
# print(list_of_names[3])
# print(len(list_of_names[3]))

name="Name"
print(f'{name:>15}',"\t\tLenght_of_name")

for name in range(len(list_of_names)):
    print(f'{list_of_names[name]:>15}','\t\t',len(list_of_names[name]))

maximum= len(list_of_names[0])
for name in range(len(list_of_names)):
    maximum=len(list_of_names[name])
    maximum_name=list_of_names[name]
print()
print(maximum_name,"with a length of", maximum, "is the largest")




# value='a'
# minimum=0
# for i in range(len(list_of_names)):
#     lenght=len(list_of_names[i])
#     if minimum>lenght:
#         minimum=lenght
#         name=list_of_names[i]
#     print(value)
#     print(minimum)

minimum= len(list_of_names[name])
for name in range(len(list_of_names)):
     if len(list_of_names[name]) < minimum:
        minimum=len(list_of_names[name])
        minimum_name=list_of_names[name]
print()
print(minimum_name,"with a length of", minimum, "is the lowest")
print()


five_characters_name_counter=0
for name in range(len(list_of_names)):
    if(len(list_of_names[name])==5):
       five_characters_name_counter+=1
       print(list_of_names[name], "has 5 characters name")
print(five_characters_name_counter,"are five characters  ")
print()


list_of_names[name].__contains__("gen")
for name in range(len(list_of_names)):
  if list_of_names[name].__contains__("gen"):
    print(list_of_names[name], "contains 'gen'                                              ")

