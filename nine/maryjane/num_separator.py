number=input("enter five digit number")
number=int (number)
if (number//10000<1 or number//10000>9):print("invalid number")
else:
 num1=number//10000
 num2=number%10000//1000
 num3=number%10000%1000//100
 num4=number%10000%1000%100//10
 num5=number%10000%1000%100%10

 print(num1, num2, num3, num4, num5)