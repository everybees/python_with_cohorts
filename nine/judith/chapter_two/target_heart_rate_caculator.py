age = int(input('Enter your age'))
maximum_heart_rate = 220 - age
target_heart_rate = 0.85 * maximum_heart_rate
target_heart_rate2 = 0.50 * maximum_heart_rate
print('Your maximum heart rate is :', maximum_heart_rate)
print('Your target heart rate between 50 - 85% is :', target_heart_rate2,  target_heart_rate)