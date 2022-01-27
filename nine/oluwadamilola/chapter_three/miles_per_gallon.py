gallon = 0
total_miles_per_gallon = 0.0
counter = 1
miles_per_gallon = 0.0

while gallon != -1:
    gallon = float(input("Enter the gallon used (or -1 to exit):  "))
    if gallon != -1:
        miles = float(input("Enter the miles driven:  "))
        miles_per_gallon = miles / gallon
        total_miles_per_gallon += miles_per_gallon
        print(f'The miles per gallon is: {miles_per_gallon:>2.4f}')
print(f'The total miles per gallon is: {total_miles_per_gallon:>2.4f}')