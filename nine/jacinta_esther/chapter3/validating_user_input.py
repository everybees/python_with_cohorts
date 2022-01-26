passes = 0
failures = 0
studentCounter = 1

while passes + failures != 10:
    result = int(input("Enter result (1=pass, 2 = fail) or -1 to exit: "))
    if result == 1:
        passes += 1
    elif result == 2:
        failures += 1

    studentCounter += 1

print("passed:", passes, "Failed: ", failures)
if passes > 8: print("Bonus to instructor!")
