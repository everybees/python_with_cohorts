class_a = ["Hellen", "Paul", "Aka", "Rogen", "Motunrayo", "olorungbemi"]
class_b = ["David", "Johnson", "Esther", "saheed", "joel", "John"]

maximum_in_class_a = max(class_a, key=len)
maximum_in_class_b = max(class_b, key=len)

minimum_in_class_a = min(class_a, key=len)
minimum_in_class_b = min(class_b, key=len)

if len(maximum_in_class_a) > len(maximum_in_class_b):
    print('Class_a longest name is', maximum_in_class_a)
else:
    print("Class_b longest name is", maximum_in_class_b)

if len(minimum_in_class_a) < len (minimum_in_class_b):
    print("Class_a shortest name is", minimum_in_class_a)
else:
    print("Class_b shortest name is", minimum_in_class_b)
# To find the shortest and longest name in two class(class_a & class_b)

#class_c = class_b + class_a

#for i in range(len(class_c)):

 #   print("This is the mininum :", class_c[i])
