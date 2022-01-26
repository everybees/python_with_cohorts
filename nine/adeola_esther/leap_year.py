year=input("Enter the year you wanna check darling  ")

year=int(year)

if year % 4==0 and year % 100 !=0:
    print("This a leap Year")

elif year%400==0:
    print("This is leap year")
else:
    print("It's not a leap year")


