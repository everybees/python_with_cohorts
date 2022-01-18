# 2.7 (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)

a = 1024
b = 4
c = 10
d = 2
if a % b == 0:
    print("yes," + str(b) + " is a multiple of " + str(a))
if a % b != 0:
    print(str(b) + " is not a multiple of " + str(a))

if c % d == 0:
    print("yes," + str(d) + " is a multiple of " + str(c))
if c % d != 0:
    print(str(d) + " is not a multiple of " + str(c))




