print("How many three digit numbers are divisible by 17")
input("Press enter to find out....")
list_0f_num = []

for number in range(1000):
    if number % 17 == 0:
        list_0f_num.append(number)

print(list_0f_num)
print(len(list_0f_num))

# continue is used to end the current iteration in a for loop or a while loop and continues the next iteration
# The break keyword is used to break out of a for/while loop

# "is" operator is used to check if two variables are located in the same part of the memory
# "==" operator is used to check of a value equals the other. Returns true or false.
