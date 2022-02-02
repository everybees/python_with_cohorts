age = int(input('Enter your age: '))
maximum_heart_rate = 220 - age
# for target heart rate
lower_bound = 0.50 * maximum_heart_rate
higher_bound = 0.85 * maximum_heart_rate
target_heart_rate = lower_bound, higher_bound

print('Maximum heart rate is', maximum_heart_rate)
print("Target heart rate is between range of", lower_bound, "-", higher_bound)
