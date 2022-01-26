digit_number=input("Enter a four digit number:   ")

digit_number=int(digit_number)

first_number=digit_number/10000
first_number=int(first_number)
# print("The value of the firstnumber is: ",first_number)

second_number=(digit_number % 10000)/1000
second_number=int(second_number)
# print("The value of the secondnumber is: ",second_number)

third_number=(digit_number % 1000)/100
third_number=int(third_number)
# print("The value of the thirdnumber is: ",third_number)

four_number=(digit_number % 100)/10
four_number=int(four_number)
# print("The value of the fournumber is:  ",four_number)

fifth_number=(digit_number % 10)/1
fifth_number=int(fifth_number)
# print("The value of the fifthnumber is: ",fifth_number)

print("this are the number ",first_number,"\t",second_number,"\t",third_number,"\t",four_number,"\t",fifth_number)