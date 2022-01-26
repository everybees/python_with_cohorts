gallon = float(input("Enter the gallon used(-1 to exit): "))
miles_per_gallon = 0
total_mile_per_gallon = 0
total_miles = 0 
total_gallons = 0

while gallon != -1:
    miles = int(input("Enter miles driven: "))
    miles_per_gallon = miles/gallon
    total_gallons += gallon
    total_miles += miles
    total_mile_per_gallon = total_miles/total_gallons
    print("The miles/gallon for this tank was ",f'{ miles_per_gallon:>.2f}')
    gallon = float(input("Enter the gallon used(-1 to exit): "))
print("The overall average miles/gallon was ",f' {total_mile_per_gallon:>.2f}')