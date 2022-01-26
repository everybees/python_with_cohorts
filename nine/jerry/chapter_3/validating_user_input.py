# 3.1 (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any
# input, if the value entered is other than 1 or 2, keep looping until the user enters a correct
# value. Use one counter to keep track of the number of passes, then calculate the number
# of failures after all the user’s inputs have been received.


passes = 0
failure = 0

counter = 1
while passes + failure != 10:
    result = int(input("Enter result: 1 for pass, 2 for fail"))
    if result == 1:
        passes += 1
    if result == 2:
        failure += 1
    counter += 1


print("Passed", passes)
print("Failed", failure)
