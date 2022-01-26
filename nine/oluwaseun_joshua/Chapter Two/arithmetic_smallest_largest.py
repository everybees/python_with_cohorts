first_number=input("Enter firstnumber: ")
second_number=input("Enter secondnumber:  ")
third_number=input("Enter thirdnumber:   ")

first_number=int(first_number)
second_number=int(second_number)
third_number=int(third_number)

sum_of_number=first_number + second_number + third_number
print("the sum of the number is",sum_of_number)

average_of_all_numbers = sum_of_number/3
print("the avearage value of the number is: ",average_of_all_numbers)

product_of_numbers = first_number * second_number * third_number
print("The product of the number is: ",product_of_numbers)

if(first_number > second_number > third_number):
    print("The firstnumber is the highest number: ",first_number)

elif(first_number < second_number < third_number):
        print("The firstnumber is the smallest number: ",first_number)


if(second_number > first_number > third_number):
    print("The secondnumber is hightest number: ",second_number)


elif(second_number < first_number < third_number):
    print("The secondnumber is smallest number: ",second_number)

if(third_number > first_number > second_number):
    print("The thirdnumber is the highest number: ",third_number)

elif(third_number < first_number < second_number):
    print("thirdnumber is the smallest number",third_number)