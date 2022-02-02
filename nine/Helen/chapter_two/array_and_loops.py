# print("Number\t      Square\t     Cube\t")
# for i in range(0, 5):
#     i = i ** 2
#     j = i**3
#     print(i, j)

















# name = "folaaaaaaaaaaEE"
# name_replaced = name.replace("a", "e")
# name_capital = name.capitalize()
# print(name_capital)


# print(name_replaced)
# print(len(name))

# list_of_name = ["Helennnnn", "janet", "maryuuuuuuuu"]
# for i in range(0, len(list_of_name), +1):
    
#     if (len(list_of_name[0]) > len(list_of_name[i]) ):
#         print(len(list_of_name[0]), "is the highest")
#     if (len(list_of_name[0]) < len(list_of_name[i]) ):
#         print(len(list_of_name[i]), "is the highest")


# value = "a"
# mininum = 1000
# for i in range(len(list_of_name)):
#     length =  len(list_of_name[i])
#     if mininum>length:
#         minimum = length
#         value = list_of_name[i]
#         print(value)
#         print(mininum)


# list_of_name.append("Malik")
# print(list_of_name)
# list_of_name.count("Malik")


class_a = ["Helen", "isutttttttttt", "Jumai", "David"]
class_b = ["otunba", "Motunrayoooooo", "Increase" , "samuel"]
longest = 0
smallest = 0
for i in range(len(class_a)):
    length = len(class_a[i])
    if longest < length:
        longest = length
        value = class_a[i]
    else:
        if i in range(len(class_b)):
            length = len(class_b[i])
            if smallest < length:
                smallest = length
                value1 = class_b[i]

print("class a longest name = ", value)
print("class i longest name = ", value1)












# class_a = ["Helen", "isu", "Jumai", "David"]
# class_b = ["otunba", "Motun", "increase", "samuel"]
# classes = [class_a,class_b]
# for i in range(len(classes)):
#     for j in range(len(classes[i])):
#         # print(classes[i][j])
#         if (i>j):
#          print(i)

#          print()

#         else:
#          print(j)
