number = input("Enter a number in 0's and 1's:  ")
for i in range(len(number)):
    if number[i] == '1' and number[i - 1] == '0':
        decimal = int(number, 2)
        print("The decimal equivalent of", number, "is", decimal)
