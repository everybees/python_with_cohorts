# 3.16 (Nested Control Statements) Use a loop to find the two largest values of 10 numbers entered.


maximum = float('-inf')
second_largest = 0
for i in range(1, 11):
    number = int(input("Enter a number: "))
    if number > maximum:
        second_largest = maximum
        maximum = number
    if number > second_largest and number < maximum:
        second_largest = number


print(maximum)
print(second_largest)
