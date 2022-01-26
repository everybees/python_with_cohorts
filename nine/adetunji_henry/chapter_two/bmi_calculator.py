height = float(input("Enter your height in meters here: "))
weight = float(input("Enter your weight in kilograms here: "))

BMI = weight / (height * height)
print("Your BMI that was calculated is: ", BMI)

if BMI > 0:
    if BMI <= 16:
        print("You are very underweight!")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 25:
        print("Congratulations! You are healthy")
    elif BMI <= 30:
        print("You are overweight")
    else:
        print("You are very overweight!")

else:
    print("enter valid details")
