# (Sort in Ascending Order) Write a script that inputs three different floating-point
# numbers from the user. Display the numbers in increasing order. Recall that an if statement’s
# suite can contain more than one statement. Prove that your script works by running
# it on all six possible orderings of the numbers. Does your script work with duplicate
# numbers? [This is challenging. In later chapters you’ll do this more conveniently and with many more numbers.]

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
num3 = float(input("Enter third number"))
if num1 > num2 > num3:
    print(num3, num2, num1)
if num1 > num3 > num2:
    print(num2, num3, num1)
if num2 > num1 > num3:
    print(num3, num1, num2)
if num2 > num3 > num1:
    print(num1, num3, num2)
if num3 > num1 > num2:
    print(num2, num1, num3)
if num3 > num2 > num1:
    print(num1, num2, num3)
