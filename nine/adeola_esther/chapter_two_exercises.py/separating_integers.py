# 2.11
value= input('Enter the digits   ')

digits=int(value)

first_digit=int(digits%10000)

second_digit=int(digits%10000/1000)

third_digit=int(digits%1000/100)

fourth_digit=int(digits%100/10)

fifth_digit=int(digits%10/1)

print( first_digit,second_digit, third_digit,fourth_digit,fifth_digit, sep="  " ,end="")