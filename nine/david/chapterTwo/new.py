num = print("Enter an even number")
sum = 0


while num != ".":
    number = int(num)
    if number % 2 == 1:
        print("Error! Only even numbers")
        num = input("Enter a number")
        continue
    sum += number
    num = input("num")
print("The sum is: ", sum)