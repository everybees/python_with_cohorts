


# Target Heart-Rate Calculator) While exercising, you can use a heart-rate monitor
# to see that your heart rate stays within a safe range suggested by your doctors and trainers.
# According to the American Heart Association (AHA) (http://bit.ly/AHATargetHeartRates),
# the formula for calculating your maximum heart rate in beats per minute is 220
# minus your age in years. Your target heart rate is 50–85% of your maximum heart rate.
# Write a script that prompts for and inputs the user’s age and calculates and displays the
# user’s maximum heart rate and the range of the user’s target heart rate.


age = int(input("Enter your age in years: "))

max_heart_rate = 220 - age

lower_bound = 0.5 * max_heart_rate
upper_bound = 0.85 * max_heart_rate

lower_bound_ = lower_bound / 100
upper_bound_ = upper_bound / 100

print("Your maximum heart rate is: ", max_heart_rate, "\n" "The lowest bound target is: ", lower_bound_,
      "The highest bound target is: ", upper_bound_)
