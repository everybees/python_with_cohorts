import math

user_input = int(input('Enter the number of terms: '))

e = 1.0

for i in range(user_input):
    e = e + (1/math.factorial(i))
    i += 1
print('e: ', e)
