total = 1
counter = 1
number_input = int(input("Enter a number:  "))
total1 = number_input + 0
while counter <= number_input:
    total *= counter
    counter += 1

if total1 > 0:
    print("The factorials of", number_input, "is", total)
else:
    print("The number is less than 1")
