age_in_years = int(input("Enter your age in years: "))
if age_in_years > 0:
    maximum_heart_rate = 220 - age_in_years
    print("Your maximum heart rate is: ", maximum_heart_rate, "beats per minute")

    target_heart_rate_lowerbound=  0.5 * maximum_heart_rate 
    target_heart_rate_upperbound=  0.85 * maximum_heart_rate 

    print("Your target heart is between ", target_heart_rate_lowerbound, "-", target_heart_rate_upperbound)