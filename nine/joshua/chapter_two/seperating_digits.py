# Author: Joshua
# Title : Separating the digits in an integer 2.11
number = int(input("Type an integer"))

first = number // 10000
num1 = number % 10000
second = num1 // 1000
num2 = num1 % 1000
third = num2 // 100
num3 = num2 % 100
fourth = num3 // 10
five = num3 % 10
print(first, second, third, fourth, five)
