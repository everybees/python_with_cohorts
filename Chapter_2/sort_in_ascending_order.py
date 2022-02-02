# (Sort in Ascending Order) Write a script that inputs three different floating-point
# numbers from the user. Display the numbers in increasing order. Recall that an if statement’s
# suite can contain more than one statement. Prove that your script works by running it on all
# six possible orderings of the numbers. Does your script work with duplicate
# numbers? [This is challenging. In later chapters you’ll do this more conveniently and with many more numbers.


digit1 = float(input("enter a number: "))
digit2 = float(input("enter a number: "))
digit3 = float(input("enter a number: "))

big = digit3
medium = digit2
small = digit1


if digit2 > digit1 and digit2 > digit3:
    big = digit2
elif digit3 > digit1 and digit3 > digit2:
    big = digit3
elif digit2 > digit3 and digit2 < digit1:
    medium = digit2
elif digit2 < digit3 and digit3 < digit1:
    medium = digit3
elif digit2 < digit3 and digit2 < digit1:
    small = digit2
elif digit3 < digit2 and digit3 < digit1:
    small = digit3
elif digit1 < digit3 and digit1 < digit2:
    small = digit1


print("Small is: ", small, "\nMedium: ", medium, "\nBig is: ", big)