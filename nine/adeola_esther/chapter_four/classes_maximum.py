class_a=["Helen", "Paul", "Joe","Rogen", "Motunrayo",]
class_b=["David", "Johnson", "Esther", "Mofobi", "John"]



maximum_a = 0
for name in range (len(class_a)):
    if (len(class_a[name])>maximum_a):
     maximum_a=len(class_a[name])
     maximum_class_a_name=class_a[name]

print()
print(maximum_class_a_name, "with a length of" ,maximum_a,  "is the longest in the class_a" )
print()

maximum_b= 0
for name in range (len(class_b)):
    if (len(class_b[name])>maximum_b):
     maximum_b=len(class_b[name])
     maximum_class_b_name=class_b[name]
print()
print(maximum_class_b_name,  "with a length of", maximum_b, "is the longest in the class_b" )
print()


if (maximum_a > maximum_b):
   print(maximum_class_a_name, "is the longest")
else:
    print(maximum_class_b_name)
    print()
