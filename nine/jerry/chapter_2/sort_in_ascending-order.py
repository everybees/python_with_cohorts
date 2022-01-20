# 2.15 (Sort in Ascending Order) Write a script that inputs three different floating-point
# numbers from the user. Display the numbers in increasing order.
# Recall that an if statement’s suite can contain more than one statement.
# Prove that your script works by running it on all six possible orderings of the numbers.
# Does your script work with duplicate numbers?
# [This is challenging. In later chapters you’ll do this more conveniently and with many more numbers.]


first_number = float(input("Enter a decimal number: "))
second_number = float(input("Enter a decimal number: "))
third_number = float(input("Enter a decimal number: "))


if first_number < second_number and first_number < third_number:
    if first_number == second_number or first_number == third_number:
        print(first_number)
    else:
        print(first_number)
elif second_number < first_number and second_number < third_number:
    if second_number == first_number or second_number == third_number:
        print(second_number)
    else:
        print(second_number)
elif third_number < first_number and third_number < second_number:
    if third_number == second_number or third_number == first_number:
        print(third_number)
    else:
        print(third_number)



if second_number < first_number < third_number or second_number > first_number > third_number:
    if first_number == second_number or first_number == third_number:
        print(first_number)
    else:
        print(first_number)
elif first_number < second_number < third_number or first_number > second_number > third_number:
    if second_number == first_number or second_number == third_number:
        print(second_number)
    else:
        print(second_number)
elif first_number < third_number < second_number or first_number > third_number > second_number:
    if third_number == second_number or third_number == first_number:
        print(third_number)
    else:
        print(third_number)



if first_number > second_number and first_number > third_number:
    if first_number == second_number or first_number == third_number:
        print(first_number)
    else:
        print(first_number)
elif second_number > first_number and second_number > third_number:
    if second_number == first_number or second_number == third_number:
        print(second_number)
    else:
        print(second_number)
elif third_number > first_number and third_number > second_number:
    if third_number == second_number or third_number == first_number:
        print(third_number)
    else:
        print(third_number)
