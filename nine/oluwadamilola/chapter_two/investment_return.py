p = 1000
r = 0.07
n1 = 10
n2 = 20
n3 = 30


# p = principal
# r = rate
# n1 = number_of_years1
# n2 = number_of_years2
# n3 = number_of_years3

a1 = p* (1 + r) ** n1
a2 = p * (1 + r) ** n2
a3 = p* (1 + r) ** n3

print("The amount on deposit for 10years is ", a1)
print("The amount on deposit for 20years is ", a2)
print("The amount on deposit for 30years is ", a3)