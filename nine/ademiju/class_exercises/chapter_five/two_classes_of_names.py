class_a = ["Helen", "Motunrayo","Paul","Joe","Rogen","Ade","Ademiju"]
class_b = ["David","Johnson","Esther","Mofobi","John","Ademijuwonlo"]


maximum_a = 0
for name in range(len(class_a)):
 if(len(class_a[name])> maximum_a):
    maximum_a = len(class_a[name])
    maximum_class_a_name = class_a[name]
print(maximum_class_a_name, 'in class_a is the longest name with length =',maximum_a)

maximum_b = 0
for name in range(len(class_b)):
 if(len(class_b[name])> maximum_b):
    maximum_b = len(class_b[name])
    maximum_class_b_name = class_b[name]
print(maximum_class_b_name, 'in class_b is the longest name with length =',maximum_b)
print()
if(maximum_a > maximum_b):
    print(maximum_class_a_name, "in class_a is the longest name of the two classes with a length of",maximum_a)
else:
    print(maximum_class_b_name, "in class_b is the longest name of the two classes with a length of", maximum_b)

print()

classes =[class_a,class_b]
maximum_classes = 0
for name_class_a in range(len(classes)):
    for name_class_b in range(len(classes[name_class_a])):
        if(len(classes[name_class_a][name_class_b]) > maximum_classes):
            maximum_classes = len(classes[name_class_a][name_class_b])
            maximum_classes_name = classes[name_class_a][name_class_b]
if(class_a.__contains__(maximum_classes_name)):
             print(maximum_classes_name,"in class_ a is the longest name of the two classes with a length of",maximum_classes)
else:
        print(maximum_classes_name,"in class_b is the longest name of the two classes with a length of",maximum_classes)        
     

