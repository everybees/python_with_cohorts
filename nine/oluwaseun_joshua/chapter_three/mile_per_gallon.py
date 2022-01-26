from lib2to3.pgen2 import driver


miles_driven=0
gallons=0
miles_per_gallon=0
total_miles =0
total_gallons =0

# Driver_input=input("Enter a number")
tankful=0
total_miles_per_gallon=0

while(miles_driven != -1):
    miles_driven=input("Enter miles driven: ")
    miles_driven=int(miles_driven)
    if(miles_driven ==-1):
        break

    gallons=input("Enter a gallons per trip: ")
    gallons=float(gallons)
   
    total_miles += miles_driven
    total_gallons += gallons

    miles_per_gallon= miles_driven / gallons
    
    print(f'The miles per gallon is { miles_per_gallon:>.2f}')
    tankful=tankful+1
    print("tankful is:  ",tankful)

total_miles_per_gallon = total_miles / total_gallons


print(f"the overall mile is: {total_miles_per_gallon:>.2f}")



