# Author: Joshua
# Title : Target heart_rate_calculator
age = int(input("Please input your age: "))
maximum_heart_rate = 220 - age
target_heart_rate_minimum = 50 / 100 * maximum_heart_rate
target_heart_rate_maximum = 80 / 100 * maximum_heart_rate
print("your target heart rate is between {} and {}".format(target_heart_rate_minimum, target_heart_rate_maximum))
