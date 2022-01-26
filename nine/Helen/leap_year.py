user = input("Enter a year")
year = int(user)
if(year % 4 ==0 and year % 100 !=0 or year % 400==0):
    print(year, "It is a Leap year")
else:
    print("it is not a leap year")