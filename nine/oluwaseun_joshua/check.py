
from operator import contains
from re import I, M, search
import sys
from unittest import result
from xmlrpc.client import boolean

from sqlalchemy import true
name="sEuN"

#it make the first letter upper case while others lower case.
# name_capatitalize=name.capitalize()

# name_lower=name.lower()

# print(name)
# print(name_capatitalize)

# print(name_lower)


# name_with_white_space= "    seun"

# name_strip=name_with_white_space.lstrip()
# print(name_strip)
# print(name_strip)        

# name_swapped=name.swapcase()
# print(name_swapped)


# list_of_names=["Helen", "Joe", "Paul", "Tola"]

# print(list_of_names[3])
# print(len(list_of_names[3]))
# print(len(list_of_names[0]))

# how to calculate the long length name
# longest_string=max(list_of_names, key=len)
# print(longest_string)

# smallest_string=min(list_of_names, key=len)
# print(smallest_string)

# longest =+1
# for name in list_of_names:
#     if  len(name) > longest:
#         longest= len(name)
#         result= name

# print(result)


# smallest=1000
# for name in list_of_names:
#     if  len(name) < longest:
#         longest= len(name)
#         result= name

# print(result)

# list_of_name=["Helen", "Paul", "Joe","Motunrayo","David", "Johnson", "Rogen" ,"Adeola Esther", "Mofobi", "John-Doe"]

# # smallest=5
# # for name in list_of_name:
# #     if len(name) ==smallest:
# #         smallest=len(name)
# #         result=name
# #         print(result)

# search="ul"
# for name in list_of_name:
#     if name.__contains__(search):
#             print(name)

class_a= ["hellen", "tolu","ruth","yusuf", "taye","motunrayo"]
class_b =["shade", "dele","faith","solomon","femi"]

longest_for_class_b=0
longest_for_class_a=0
for name in class_a:
     if len(name)>longest_for_class_a:
         longest_for_class_a=len(name)
         result1=name
# print(result1)



# longest_for_class_b=0
for name in class_b:
    if len(name)>longest_for_class_b:
        longest_for_class_b=len(name)
        result2=name
# print(result2)




if (len(result1 )> len(result2)):
    print(result1)
else:
    print(result2)


classes=[class_a,class_b]
# maximum=0
# # minimum=0

# for i in range(len(classes)):
#     for j in range (len(classes[i])):
#         # print(classes[i][j]) 

#         if(i>j):
#             print("class A is the highest number")
#         else:
#             print (j)

# # for i in range (len(class_a)):
# #     for j in class_a (len(class_a)):
# #         print(class_a[class_b])
