year= int(input("Enter a year to check for: "))

if(year % 4 == 0):
    if( year % 400 == 0):
        print("This is a leap year")
    
    elif(year % 100 == 0):
            print("This is a leap year")
    else:
        print("This is not a leap year")
else:
    print("This is not a leap year")