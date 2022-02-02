first_number=0
second_number=0
third_number=0
forth_number=0
fifth_number=0
 
  
for number in range (1):
   userInput = input("Enter five integer")
   userInput=int(userInput)
   
   fifth_number= int(userInput/10000)
   
   forth_number = int(userInput% 10000/1000)
  
   third_number = int(userInput% 1000/100)

   second_number = int(userInput% 100/10)
   
   first_number = int(userInput% 10/1)


print("the five integers are: ",first_number,second_number,third_number,forth_number,fifth_number)

if(fifth_number==first_number and first_number==fifth_number):
    print("It a panlindrome")

else:
    print("Not a panlindrome")


if(forth_number==second_number and second_number==forth_number):
	    print("it is a palindrome")

else:
    print("Not a panlindrome")
