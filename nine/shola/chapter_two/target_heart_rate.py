# (Target Heart-Rate Calculator) While exercising, you can use a heart-rate monitor
# to see that your heart rate stays within a safe range suggested by your doctors and trainers.
# According to the American Heart Association (AHA) (http://bit.ly/AHATargetHeart-
# Rates), the formula for calculating your maximum heart rate in beats per minute is 220
# minus your age in years. Your target heart rate is 50–85% of your maximum heart rate.
# Write a script that prompts for and inputs the user’s age and calculates and displays the
# user’s maximum heart rate and the range of the user’s target heart rate

age = input("Enter your age in years")
max_heart_rate = 220 - (int(age))
target_heart_rate = 0.7 * max_heart_rate

print("your age is: ", age)
print("your maximum heart rate is: ", max_heart_rate)
print("your target heart rate is: ", target_heart_rate)

