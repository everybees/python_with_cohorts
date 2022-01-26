a_List = []

for number in range(1, 11):#puts the numbers in a list
    a_List += [number] #makes number increase inside of list

print("The value of this list is:", a_List)

print("\n Accesing values by iteration")

for item in a_List: #prints content of list
    print (item)
print()

print("\n Accesiing values by index:")
print("Subscript Value")

for i in range(len(a_List)):
    print ("%9d %7d" % (i, a_List[i]))# prints the elements in a list and its indexes

print("\n Modifying a Listr ...")
print("Value of a list before modification:", a_List)
a_List[0] = -100
a_List[4] = 19
print ("Value of aList after modification:", a_List)