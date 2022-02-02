name = "JuDiTh"
name_capitalize = name.capitalize()
name_lower = name.lower()
print(name)
# print(name_capitalize)
print(name_lower)
list_of_names = ['Helena', 'Paul', 'Joe', 'Joy', 'Sarah']
# print(list_of_names)
# print(len(list_of_names[4]))
# print(max(list_of_names, key=len))
# for i in range(len(list_of_names)):
#     if len(list_of_names[i]) == 3:
#         print(list_of_names[i])

# for j in range(len(list_of_names)):
#     first_name = len(list_of_names[0])
#     if len(list_of_names[j]) >= first_name:
#         print(list_of_names[j])


for k in range(len(list_of_names)):
    if list_of_names[k].__contains__("lena"):
        print(list_of_names[k])

class_one = ["Ramsey", "Osinakachukwu", "ThankGod", "Flourish", "Nimi"]
class_two = ["Hannah", "Juliet", "Maryann", "Mercy", "Gloria", "Cynthia", "Ayoade",'jo']

maximum_in_class_one = max(class_one, key=len)
maximum_in_class_two = max(class_two, key=len)

minimum_in_class_one = min(class_one, key=len)
minimum_in_class_two = min(class_two, key=len)

if len(maximum_in_class_one) > len(maximum_in_class_two):
    print('The longest word is in class_one', maximum_in_class_one)
else:
    print('The longest word in class i is', maximum_in_class_two)

if len(minimum_in_class_one) < len(minimum_in_class_two):
    print('The shortest word in class one is', minimum_in_class_one)
else:
    print('The shortest word in class two is', minimum_in_class_two)