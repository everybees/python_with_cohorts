def calculate_products(myList):
    product = 1
    for value in myList:
        product *= value
    return product


number_list = []
count = int(input('Enter the number of input: '))
for i in range(0, count):
    user_input = int(input("Enter A Number:"))
    number_list.append(user_input)

print(calculate_products(number_list))
