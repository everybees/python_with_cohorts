class_a = ['Helen','Paul','Joe','Rogen','Motunrayo','Ade','Oluwadunnsin']
class_b = ['David','Johnson','Esther','Mofobi','John','Ademijuwonlolois','lois']

classes=[class_a,class_b]

maximum_a = 0
for name in range(len(class_a)):
    if len(class_a[name]) > maximum_a:
        maximum_a = len(class_a[name])
        maximum_name_class_a = class_a[name]

print("From class_a",maximum_name_class_a ,"has the longest length of", maximum_a)
print()

maximum_b = 0
for name in range(len(class_b)):
    if len(class_b[name]) > maximum_b:
        maximum_b = len(class_b[name])
        maximum_name_class_b = class_b[name]

print("From class_b",maximum_name_class_b,"has the longest length of",maximum_b)
print()

if maximum_a > maximum_b:
    print(maximum_name_class_a,"has the longest length from class_a with a length of", maximum_a)
else:
    print(maximum_name_class_b, "has the longest length from class_b with a length of", maximum_b)


print()
print(classes)
print()

maximum = 0
for name in range(len(classes)):
    for names in range(len(classes[name])):
        # print(classes[name][names])
        if len(classes[name] [names]) > maximum:
             maximum = len(classes[name][names])
             maximum_name = classes[name][names]

print(maximum_name, "has the longest name of the two classes with a length of", maximum)

print()

if (class_a).__contains__(maximum_name):
        print(maximum_name,"has the longest name with length of",maximum,'which exists in class_a')
else:
        print(maximum_name,"has the longest name with length of",maximum,'which exists in class_b')