# Factorials!!


number = int(input('Enter a number: '))
factorial = 1

if number == 0 or number == 1:
     print(factorial)
if number >= 2:
    for i in range (number, 0,-1):
      factorial *= i
print(factorial)    
