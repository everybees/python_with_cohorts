# 3.15 (Challenge: Approximating the Mathematical Constant e)
# Write a script that estimates the value of the mathematical constant e by using the formula below.
# Your script can stop after summing 10 terms.


result = 0
answer = 1
integer = int(input("Enter the number of terms: "))
for digit in range(integer):
    for number in range(0, digit):
        answer *= (integer - number)
    result += 1 / answer

e = 1 + result
print(f"The constant's estimate after {integer} is {e}")

