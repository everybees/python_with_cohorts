binary_number = input("Enter binary number")
counter = 0
base_number = 10
total = 0

while counter < len(binary_number):
    number = int(binary_number)
    each_number = number % (base_number ** counter+1)//(base_number ** counter+1)
    print(each_number)
    counter+=1