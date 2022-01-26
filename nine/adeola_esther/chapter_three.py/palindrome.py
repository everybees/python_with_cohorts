# 3.12

user= int(input("Enter the numbers:  "))

first_number= int(user%10000)
second_number= int(user%10000)/1000
third_number= int(user%1000)/100
fourth_number= int(user%100)/10
fifth_number= int(user%10)

# print(first_number,second_number,third_number,fourth_number,fifth_number)
print()

if (first_number == fifth_number and second_number == fourth_number):
    print('It is Palindrome')
# else: #(int(first_number!=fifth_number and second_number!=fourth_number))
    print('It is not a Palindrome')