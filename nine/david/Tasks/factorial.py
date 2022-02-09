number = int(input("Enter a number to check factorial: "))
factorial = 1
    
for num in range(1, number + 1):
    factorial = factorial * num
print(factorial)

if (number == 0):
    print("Factorial of 0 is ", factorial)
elif(number == 1):
    print("Factorial of 1 is ", factorial)
