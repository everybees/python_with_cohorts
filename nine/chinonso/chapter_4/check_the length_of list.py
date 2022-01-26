
# names = ['Helen','Paul','Joe','Motunrayo','David','Johnson']
# maxi = len(names[0])
# for i in range (len(names)):
#     if len(names[i]) < maxi:
#         maxi = len(names[i])
# print(names[maxi])


class_a = ['chinonso','esther','joe','candy']
class_b = ['oyinyechi','ugochi','chidinma','kachi']

length =0
for i in class_a,class_b:
    for j in i:
        if len(j)>length:
            length = len(j)
            word =j
            position = i.index(j)
print(word, position)
