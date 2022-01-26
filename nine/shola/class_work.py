class_a = ['Shola', "Musa", 'Ademiju', 'Otunba', 'Helen', 'Tolu']
class_b = ['Motunrayo', 'Judith', 'Olamide', 'Adetunji', 'Ayo', 'Lekan']

# maximum_a = max(class_a, key=len)
# minimum_a = min(class_a, key=len)
#
# maximum_b = max(class_b, key=len)
# minimum_b = min(class_b, key=len)
#
# overall_max = max(maximum_a, maximum_b)
# overall_min = min(minimum_a, minimum_b)
#
# print(overall_max)
# print(overall_min)
#

classes = [class_a, class_b]
for i in range(len(classes)):
    for j in range(len(classes[i])):
        print(classes[i][j],  len(classes[i][j]))