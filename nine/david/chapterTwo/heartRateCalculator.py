age = int(input("Enter your age: "))

maximum_heart_rate = 220 - age
target_heart_rate = 85|100 * maximum_heart_rate
target_heart_rate_range = 0

for i in range(0, target_heart_rate):
    target_heart_rate_range += target_heart_rate

print("Maximum heart Rate = ", maximum_heart_rate)
print("Your targe heart rate = ", target_heart_rate)
print("Your target heart range = ", target_heart_rate_range, end=" ")

