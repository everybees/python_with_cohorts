passes = 0
failures = 0
number_of_failures = 0

for students in range(10):
    result = int(input("Enter results (1 = pass. 2 = fail: )"))


    if result == 1:
        passes += 1
    elif result != 1 and result != 2:
        print("Invalid input")
    else:
        failures += 1


print("Passes = ", passes)
print("Failures = ", failures)