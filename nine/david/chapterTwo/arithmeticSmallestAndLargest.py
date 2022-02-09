print("This program prints the sum, product, average, smallest and largest of your inputs")
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter tnird number: "))
print()

sum = input1 + input2 + input3
average = sum / 3
product = input1 * input2 * input3

if input1 < input2 and input1 < input3:
    smallest = input1
elif input2 < input3:
    smallest = input2
else:
    smallest = input3

if input1 > input2 and input1 > input2:
    highest = input1
elif input2 > input3:
    highest = input2
else:
    highest = input3


print("The sum of your inputs = ", sum)
print("The average of your inputs = ", average)
print("The product of your inputs = ", product)
print("Smallest of your inputs = ", smallest)
print("Highest of your inputs = ", highest)
