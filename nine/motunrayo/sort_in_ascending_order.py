one = float(input("Please input a number : "))
two = float(input("Please input a second number : "))
three = float(input("Please input a third number : "))

if one < two and three < two:
    if one > three:
        print(three, one, two)
    else:
        print(one, three, two)
elif one < three and two < three:
    if one > two:
        print(two, one, three)
    else:
        print(one, two, three)        
elif two < one and three < one:
    if three > two:
        print(two, three, one)
    else:
        print(three, two, one)
else:
    print(one, two, three)