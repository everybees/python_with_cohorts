# 3.21 (Calculate Change Using Fewest Number of Coins) Write a script that inputs a
# purchase price of a dollar or less for an item. Assume the purchaser pays with a dollar bill.
# Determine the amount of change the cashier should give back to the purchaser. Display
# the change using the fewest number of pennies, nickels, dimes and quarters. For example,
# if the purchaser is due 73 cents in change, the script would output:
# Your change is:
# 2 quarters
# 2 dimes
# 3 pennies


for count in range(1, 6):
    number = int(input("Enter a number that is not less than 1 or greater than 100: "))
    if number > 0 or number <= 100:
        numbers = number // count
