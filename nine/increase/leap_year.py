year = input("Enter a year: ")
leap_year = int(year)
    
    #year can be evenly divided by 100, it is NOT a leap year unless the year can be evenly divided by 100,
    #it is NO
if(leap_year % 4 == 0):
    if(leap_year % 100 >= 1 ):
        print("This is a leap year")
  
    elif(leap_year % 400 == 0):
            print("This is a leap year")
    else:
        print("This is not a leap year")
else:
      print("This is not a leap year")