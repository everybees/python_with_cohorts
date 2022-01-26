problem = input("What is your problem")

confirmation = input("Have you had this problem before (yes or no)")

if confirmation.startswith('y'):
    print("Well you have it again")
else:
    print('Well, you have it now.')
