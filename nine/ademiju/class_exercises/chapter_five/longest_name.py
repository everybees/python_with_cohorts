list_of_names  = ["Helen","Paul","Increase","Motunrayo","Ademijuwonlo","Adeola-Esther","Joe","Mary-Jane","Jane-Doe","Rogen","David"]
name = "Name"
print(f'{name:>15}',"\t\tLength_of_name")
for name in range(len(list_of_names)):
  print(f'{list_of_names[name]:>15}','\t\t' ,len(list_of_names[name]))
maximum = 0
for name in range(len(list_of_names)):
 if(len(list_of_names[name])> maximum):
     maximum = len(list_of_names[name])
     maximum_name = list_of_names[name] 
print()
print(maximum_name,"is the longest name with a length of", maximum,)
print()

minimum = 1000
for name in range(len(list_of_names)):
 if(len(list_of_names[name])< minimum):
     minimum = len(list_of_names[name])
     minimum_name = list_of_names[name] 
print()
print(minimum_name,"is the shortest name with a length of",minimum)
print()

five_lettered_name_counter = 0
for name in range(len(list_of_names)):
 if(len(list_of_names[name])== 5):
     five_lettered_name_counter +=1
     print(list_of_names[name],"is a 5-lettered name")
print(five_lettered_name_counter,"names are five-lettered")
print()

for name in range(len(list_of_names)):
 if list_of_names[name].__contains__("gen"):
     print(list_of_names[name],"contains 'gen'")



