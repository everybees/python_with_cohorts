user_input = int(input("Enter a number: "))

# if user_input == 1 or user_input == 2:
#     print("Success")
count = 0
total = 0
while user_input != 1 and user_input != 2:
    print("Try again")
    count += 1
    user_input = int(input("Enter a number: "))
if count == 0:
    print("You got it right at first try")
else:
    print("It took you {}".format(count), "tries")

# print("{:.2f}".format(13.94356879))

