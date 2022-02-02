# 4.9 (Temperature Conversion) Implement a fahrenheit function that returns the
# Fahrenheit equivalent of a Celsius temperature. Use the following formula:
# F = (9 / 5) * C + 32
# Use this function to print a chart showing the Fahrenheit equivalents
# of all Celsius temperatures in the range 0–100 degrees.
# Use one digit of precision for the results. Print the outputs in a neat tabular format.


def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit


print("Celsius In Degrees\tFahrenheit In Degrees\n")
for celsius in range(101):
    print(celsius, end="\t\t\t\t\t")
    print(f"{celsius_to_fahrenheit(celsius):.1f}")
    print()