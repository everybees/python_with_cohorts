year = 1992

# if ((year%4 ==0 and year%100 != 0) or (year%4==0 and year%400 == 0)):
#     print("It is a leap year")
# else:
#     print("Not a leap year")

if(year % 4 ==0):
    if(year % 100 == 0):
        # print("Not leap")
        if(year % 400 == 0):
            print("Leap year")
    else:
        print("Not leap")
        