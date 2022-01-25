name = input("Enter your name")
age = int(input("Enter your age"))
target_heart_rate = 220 - age
print("Your target rate is ",target_heart_rate)

print("Your maximum heart rate is", 0.5 * target_heart_rate ,  "-", 0.85 * target_heart_rate)
