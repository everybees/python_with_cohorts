# 3.11 (Miles Per Gallon) Drivers are concerned with the mileage obtained by their automobiles.
# One driver has kept track of several tankfuls of gasoline by recording miles driven
# and gallons used for each tankful. Develop a sentinel-controlled-repetition script that
# prompts the user to input the miles driven and gallons used for each tankful. The script
# should calculate and display the miles per gallon obtained for each tankful.
# After processing all input information, the script should calculate and display the combined miles per
# gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).


total = 0
miles = 0
gallons_used = 0
while miles != -1:
    miles = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of diesel gallons used: "))
    if miles == -1:
        break
    miles_per_gallon = gallons_used / miles
    print(f'The miles per gallon for this tank was {miles_per_gallon:.2f}')
    total += miles_per_gallon

print(f'Total miles per gallon is {total:.2f}')
