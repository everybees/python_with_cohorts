#1. Take integer variable year
#2. Assign a value to the variable
#3. Check if the year is divisible by 4 but not 100, DISPLAY "leap year"
#4. Check if the year is divisible by 400, DISPLAY "leap year"
#5. Otherwise, DISPLAY "not leap year

year = int(input("Enter a year"))
if year%4== 0 and year%100 != 0:
        print("Leap year")
elif year%400==0:
        print("leap year")
else:
    print("Not leap year")


