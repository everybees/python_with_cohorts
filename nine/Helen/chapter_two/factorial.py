number =  input("Enter a number")
number_1 = int(number)
factorial = 1

for i in range (number_1):
    if (number_1 ==0 and number_1 ==1 ):
        print(1)

    if(number_1>=2):
            factorial *= number_1
            number_1 -=1
            
print(factorial)


    

    


    
