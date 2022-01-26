# (7% Investment Return) Some investment advisors say that it’s reasonable to expect
# a 7% return over the long term in the stock market. Assuming that you begin with
# $1000 and leave your money invested, calculate and display how much money you’ll have
# after 10, 20 and 30 years. Use the following formula for determining these amounts:
# a = p(1 + r)n
# where
# p is the original amount invested (i.e., the principal of $1000),
# r is the annual rate of return (7%),
# n is the number of years (10, 20 or 30) and
# a is the amount on deposit at the end of the nth year.

principal = 1000
rate = 7*0.01
number_of_years = 10
amount_on_deposit = principal * ((1 + rate)**number_of_years)
print("Amount on deposit after",number_of_years,"years is",amount_on_deposit)
number_of_years = 20
amount_on_deposit = principal * ((1 + rate)**number_of_years)
print("Amount on deposit after",number_of_years,"years is",amount_on_deposit)
number_of_years = 30
amount_on_deposit = principal * ((1 + rate)**number_of_years)
print("Amount on deposit after",number_of_years,"years is",amount_on_deposit)

