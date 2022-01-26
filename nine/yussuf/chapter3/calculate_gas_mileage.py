total_gallon_used = 0
total_miles_driven = 0
total_MPG = 0
count = 0


milesDriven = float(input("Enter miles driven "))

while milesDriven != -1:
    gallons = float(input("Enter gallons "))
    miles_per_gallons = milesDriven/gallons
    total_gallon_used = total_gallon_used + gallons
    total_miles_driven = total_miles_driven + milesDriven
    total_MPG = total_MPG + miles_per_gallons
    print("The MPG for this trip ",miles_per_gallons)
    milesDriven = float(input("Enter miles driven "))
    count = count + 1
    
if count != 0:
    print("The total miles driven ",total_miles_driven)
    print("The MPG is ",miles_per_gallons)
    print("The total MPG is ",total_MPG)
    print("The total gallon used ",total_gallon_used)
else:
    print("Oga you no input anyting")
    