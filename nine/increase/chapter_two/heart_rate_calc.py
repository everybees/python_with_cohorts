# (Target Heart-Rate Calculator) While exercising, you can use a heart-rate monitor
# to see that your heart rate stays within a safe range suggested by your doctors and trainers.
# According to the American Heart Association (AHA) ( http://bit.ly/AHATargetHeart-
# Rates ), the formula for calculating your maximum heart rate in beats per minute is 220
# minus your age in years. Your target heart rate is 50–85% of your maximum heart rate.
# Write a script that prompts for and inputs the user’s age and calculates and displays the
# user’s maximum heart rate and the range of the user’s target heart rate. [These formulas
# are estimates provided by the AHA; maximum and target heart rates may vary based on
# the health, fitness and gender of the individual. Always consult a physician or qualified
# healthcare professional before beginning or modifying an exercise program.]


your_age = int(input('Enter your age: '))
heart_rate_per_minute = 220 - your_age
print('Your heart rate per minute is: ',heart_rate_per_minute)

minimum_target_heart_rate = 0.50  * heart_rate_per_minute
maximum_target_heart_rate = 0.85  * heart_rate_per_minute

print('Your target heart rate range is between: ', minimum_target_heart_rate,'to',maximum_target_heart_rate)


