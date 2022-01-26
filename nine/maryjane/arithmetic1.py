import  math



num1=input("enter first integer")
num2=input("enter second number")
num3=input("enter third number")

num1=int(num1)
num2=int(num2)
num3=int(num3)


print("maximum is ", num1 if (num1>num2 and num1>num3) else num2 if (num2>num1 and num2>num3) else num3)

print("minimum is ", num1 if (num1<num2 and num1<num3) else num2 if (num2<num1 and num2<num3) else num3 )













































# minimum=min(num1,min(num2, num3))
# maximum=max(num1, max(num2, num3))
# print(" the minimum number is ", minimum, "and the maximum number is ", maximum)
# minimum=num2
# maximum=num2
# if (num3<minimum and num2>minimum):minimum=num3
# if(num3>maximum and num2<maximum):maximum=num3

# elif(num2<minimum and num3>minimum):minimum=num2
# elif(num2>maximum and num3<maximum):maximum=num2
# print()
# elif (num1<minimum and num2>minimum):minimum=num1
# elif(num1>maximum and num2<maximum):maximum=num1
# print()


