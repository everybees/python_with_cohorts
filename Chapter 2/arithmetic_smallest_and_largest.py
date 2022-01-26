# (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.

sum = 0
product = 0
average = 0
smallest = 0
largest = 0


for i in range(0, 3):
    display = int(input("Enter 3 integers: "))
    sum += display

print(sum)
# print(min(display))
# print(max(display))
print(sum/3)

