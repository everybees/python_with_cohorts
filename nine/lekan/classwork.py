
class_a = ['Helen', 'Paul', 'Joe', 'Rogen', 'Motunrayo']
class_b = ['David', 'Johnson', 'Esther', 'Mofobi', 'John',]

maximum_in_class_A = max(class_a, key=len)
maximum_in_class_b = max(class_b, key=len)

minimum_in_class_a = min(class_a, key=len)
minimum_in_class_b = min(class_b, key=len)

if len(maximum_in_class_A) > len(maximum_in_class_b):
    print('class_a has the longest name which is', maximum_in_class_A)
else:
    print('class_b has the longest name which is ', maximum_in_class_b)

if len(minimum_in_class_a) < len(minimum_in_class_b):
    print('class a has the shortest name which is ', minimum_in_class_a)
else:
    print('class i has the shortest name which is', minimum_in_class_b)
