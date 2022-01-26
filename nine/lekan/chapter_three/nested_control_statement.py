largest = 0
second_largest = 0
for i in range(10):
    user_input = int(input('Enter a  number: '))

    if largest < user_input:
        largest = user_input

print('The largest number is', largest)
print('The second largest number is', second_largest)