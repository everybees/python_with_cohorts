from sys import displayhook


print("What is your problem?")

user_input=input("enter your answer here: ")

print()

print("have you had this problem before(yes or no)?")

user_response=input("what is your response:  ")
user_response.upper()

if(user_response== "Yes"):
    print("Well, you have it again.")

elif(user_response == "No"):
    print("Well, you have it now")

