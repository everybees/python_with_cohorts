# # def square(y):
# #     return y*y

# # for x in range(1, 11):
# #      print (square(x)),
# #      print()
     
# from calendar import c


def maximum_value(x, y, z):
    maximum = x

    if y > maximum:
      maximum = y

    else: 
       z > maximum
       maximum = z

    return maximum

a = int(input("enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
 
print("maximum integer is ", maximum_value(a,b,c))
print()

# import random
# for i in range(1, 21):
#   print("%10d" % random.randrange(1,7), end = ''),
#   if i % 5 == 0:
#     print()
