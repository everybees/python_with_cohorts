user=input("enter a year: ")

year=int(user)

# if(year % 4 ==0 and year % 100 !=0 or year % 400==0):
#     print(year,"It a leap year")

# else:
#     print("it's not a leap year")

if(year % 4==0):
    if(year % 100 !=0):
        if(year % 400==0):
                  print("It is a leap")
else:
    print("it not a leap year")
