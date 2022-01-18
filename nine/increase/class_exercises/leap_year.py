#Leap_year
#If year can be divided by 4... it is a leap_year,
#if year is not divisible by 100... it is NOT  a leap_year,
#and if year is divisible by 400... it is a leap_year.

year = input("Enter a year to check for : ")
leap_year = int(year)
    
    
if(leap_year % 4 == 0):
    if(leap_year % 100 >= 1 ):
        print("This is a leap year")
  
    elif(leap_year % 400 == 0):
            print("This is a leap year")
    else:
        print("This is not a leap year")
else:
      print("This is not a leap year")