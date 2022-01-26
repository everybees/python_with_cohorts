class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hi there! Welcome to Merit's Deposit & Withdrawal Machine, how may i be of help?")

    def deposit(self):
        amount = float(input("Enter the amount to be deposited: "))
        self.balance += amount
        print("\nThe amount deposited is: ", amount)

    def withdrawal(self):
        amount = float(input("Enter the amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou have been debited with: ", amount)
        else:
            print("\nWithdrawal amount exceeded account balance ")

    def display(self):
        print("\nYour available balance is: ", self.balance)


self = Bank_Account()

self.deposit()
self.withdrawal()
self.display()
