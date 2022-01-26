age = int(input("Enter your age: "))
max_heart_rate = 220 - age
print("Maximum heart rate is: ", max_heart_rate)

target_heart_rate_min = (50 * max_heart_rate)/100
target_heart_rate_max = (85 * max_heart_rate)/100

print("the range of your target heart rate is between: ", target_heart_rate_min, "and ", target_heart_rate_max)
