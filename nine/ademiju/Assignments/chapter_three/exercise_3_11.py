# (Miles Per Gallon) Drivers are concerned with the mileage obtained by their automobiles.
# One driver has kept track of several tankfuls of gasoline by recording miles driven
# and gallons used for each tankful. Develop a sentinel-controlled-repetition script that
# prompts the user to input the miles driven and gallons used for each tankful. The script
# should calculate and display the miles per gallon obtained for each tankful. After processing
# all input information, the script should calculate and display the combined miles per
# gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).
miles_driven = int(input("Enter the miles driven or -1 to exit: "))
gallon_used = int(input("Enter the gallon used or -1 to exit: "))
total_miles_per_gallon = 0
input_counter = 0

while miles_driven != -1:
    input_counter += 1
    miles_per_gallon = miles_driven / gallon_used
    total_miles_per_gallon += miles_per_gallon
    print("The miles per gallon for this tankful is: ",miles_per_gallon)
    miles_driven = int(input("Enter the miles driven or -1 to exit: "))
    gallon_used = int(input("Enter the gallon used or -1 to exit: "))

if input_counter > 0:
    overall_average_miles_per_gallon = total_miles_per_gallon / input_counter
    print("The overall average miles per gallon  driven for all tankful is",overall_average_miles_per_gallon)
else:
    print("No input was entered")
