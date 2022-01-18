# Exercise 2.25

def square_of_a_number(number):
    new_Number = int(number)
    square = 1
    if new_Number > 0:
        for i in range (new_Number):
            square = square * new_Number
    return square
    

first_user_input = input("Enter number: ")
first_user_square = square_of_a_number(first_user_input)

second_user_input = input("Enter number: ")
second_user_square = square_of_a_number(second_user_input)

difference_of_the_users_square = first_user_square - second_user_square
sum_of_the_users_square = first_user_square + second_user_square

print("This is the square of user1 input: ",first_user_square)
print("This is the square of user2 input: ",second_user_square)
print("This is the difference of user1 and user2 square : ",difference_of_the_users_square)
print("This is the sum of user1 and user2 square : ",sum_of_the_users_square)






