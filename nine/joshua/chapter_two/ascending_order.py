# Author: Joshua
# Title : Sorting in ascending order 2.15

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
if (first > second) and (first > third):
    print("First digit is the Highest ", first)

if (second > first) and (second > third):
    print("Second digit is the Highest ", second)

if (third > second) and (third > first):
    print("Third digit is the Highest ", third)

if (first > second) and (first < third):
    print("First digit is the Second ", first)
if (first < second) and (first > third):
    print("First digit is the Second ", first)

if (second < first) and (second > third):
    print("Second digit is the Second ", second)
if (second > first) and (second < third):
    print("Second digit is the Second ", second)

if (third < second) and (third > first):
    print("Third digit is the Second ", third)
if (third > second) and (third < first):
    print("Third digit is the Second ", third)

if(first < second) and (first < third):
    print("First digit is the Third ", first)

if(second < first) and (second < third):
    print("Second digit is the third ", second)

if(third < second) and (third < first):
    print("Third digit is the Third ", third)
