
gallon = 0
total_miles_per_gallon = 0
counter = 1
miles_per_gallon = 0

while gallon != -1:
    gallon = float(input("Enter the gallon used (or -1 to exit):  "))
    if gallon != -1:
        miles = float(input("Enter the miles driven:  "))
        miles_per_gallon = miles / gallon
        total_miles_per_gallon += miles_per_gallon
        print()
        print("The miles per gallon is: ", end="")
        print(f'{miles_per_gallon:>2.2f}')
        print()
print("The total miles per gallon is: ", end="")
print(f'{total_miles_per_gallon:>2.2f}')
