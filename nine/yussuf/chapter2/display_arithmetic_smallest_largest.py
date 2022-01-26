first_input = int(input("Enter number: "))
second_input = int(input("Enter number: "))
third_input = int(input("Enter number: "))

sum = first_input + second_input + third_input
average = sum / 3
product = first_input * second_input * third_input

def find_smallest_among3_integer(first_Number,second_Number,third_Number):
    smallest = first_Number
    if second_Number < smallest: smallest = second_Number
    if third_Number < smallest: smallest = third_Number
    return smallest

def find_largest_among3_integer(first_Number,second_Number,third_Number):
    largest = first_Number
    if second_Number > largest: largest = second_Number
    if third_Number > largest: largest = third_Number
    return largest

print("The sum is ",sum)
print("The average is ",average)
print("The product is ",product)
print("The smallest is ",find_smallest_among3_integer(first_input,second_input,third_input))
print("The largest is ",find_largest_among3_integer(first_input,second_input,third_input))