# Compare two user input, return true if theire equals and return false if not equal

user1 = input("Enter first value")
user2 = input("Enter second value")

user1_input = int(user1)
user2_input = int(user2)

if(user1_input == user2_input):
    print("True")
else:
    print("False")