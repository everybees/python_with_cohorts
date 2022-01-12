Year = int(input("Which year would you like to check "))

if Year % 4 == 0:
    if Year % 100 >= 1:
        print("It is a Leap Year")
    elif Year % 400 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap Year")
else:
    print("It is not a leap Year")