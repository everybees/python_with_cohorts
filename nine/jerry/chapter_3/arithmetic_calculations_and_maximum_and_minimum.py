# 3.8 (Arithmetic, Smallest and Largest) In Exercise 2.10, you wrote a script that input
# three integers, then displayed the sum, average, product, smallest and largest of those values.
# Reimplement your script with a loop that inputs four integers.

minimum = float('inf')
maximum = float('-inf')
total = 0
product = 1
for numbers in range(4):
    number = int(input("Enter an integer: "))
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
    total = number + total
    product *= number

print("The maximum number is", maximum)
print("The minimum is", minimum)
print("The sum is", total)
print("The average is", total/4)
print("The product is", product)

