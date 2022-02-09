class_a = ['Increase', 'Jerry', 'Jibola', 'Adeola','Tolulope', 'Ademijuwonlo']
class_b = ['Chinonso', 'Adetunji', 'Oluwadamilola', 'Lotachi', 'Ademiju']

# classes = [class_a, class_b]
# for i in range (len(classes)):
#     for j in range (len(classes[i])):
#         length = len(classes[i])

# class_a.extend(class_b)
# print(class_a)
# print(max(class_a, key= len))

longest_name_in_class_a = 0
longest_name_in_class_b = 0

for i in range (len(class_a)):
    if len(class_a[i]) >= longest_name_in_class_a:
        longest_name_in_class_a = len(class_a[i])
        name_in_a = class_a[i]
print(name_in_a)

for i in range (len(class_b)):
    if len(class_b[i]) >= longest_name_in_class_b:
        longest_name_in_class_b = len(class_b[i])
        name_in_b = class_b[i]
print(name_in_b)

if longest_name_in_class_a > longest_name_in_class_b:
    print(f'The longest name in both classes is {name_in_a} from class a')
elif longest_name_in_class_a == longest_name_in_class_b:
    print(f'{name_in_a} and {name_in_b} are the same length from class a and b respectively')
else:
    print(f'The longest name in both classes is {name_in_b} from class b')