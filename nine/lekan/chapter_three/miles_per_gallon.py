total = 0
user_input = 0
while user_input != -1:
    user_input = float(input('Enter the gallons used(-1 to end): '))
    miles_driven = float(input('Enter the miles driven: '))

    miles_per_gallon = miles_driven / user_input
    total += miles_per_gallon
    print('The miles/ gallons for this tank is ', miles_per_gallon)

print('The overall average miles/gallon was ', total)
