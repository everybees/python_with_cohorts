user_input = float(input("Enter A Number: "))
second_user_input = float(input("Enter A Number: "))
third_user_input = float(input("Enter A Number: "))
largest = 0
if user_input > second_user_input and user_input > third_user_input:
    largest = user_input
elif second_user_input > user_input and second_user_input > third_user_input:
    largest = second_user_input
else:
    largest = third_user_input
