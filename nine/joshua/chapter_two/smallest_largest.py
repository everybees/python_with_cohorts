# Author: Joshua
# Title : Arithmetic, Smallest and Largest 2.10
first_number = int(input("Write The first integer: "))
second_number = int(input("Write The Second integer: "))
third_number = int(input("Write The Third integer: "))

addition = first_number + second_number + third_number
product = first_number * second_number * third_number
average = (first_number * second_number * third_number) / 3
print("The total is: ", addition, "\nThe Factor: ", product,
      "\nThe Total Average is: ", average,)

if first_number < second_number and first_number < third_number:
    print(first_number, "Is The Smallest Number")
elif second_number < first_number and second_number < third_number:
    print(second_number, "Is The Smallest Number")
else:
    print(third_number, "Is The Smallest Number")

if first_number > second_number and first_number > third_number:
    print(first_number, "Is The largest Number")
elif second_number > first_number and second_number > third_number:
    print(second_number, "Is The Largest Number")
else:
    print(third_number, "Is The Largest Number")
