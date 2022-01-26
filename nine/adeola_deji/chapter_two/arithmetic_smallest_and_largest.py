firstInteger = int(input("Enter first digit: "))
secondInteger = int(input("Enter second digit: "))
thirdInteger = int(input("Enter third digit: "))

sum = firstInteger + secondInteger + thirdInteger
average = (firstInteger + secondInteger + thirdInteger)/3
product = firstInteger * secondInteger * thirdInteger

smallest = firstInteger
if secondInteger < firstInteger and secondInteger < thirdInteger:
    smallest = secondInteger
if thirdInteger < firstInteger and thirdInteger < secondInteger:
    smallest = thirdInteger

largest = firstInteger
if secondInteger > firstInteger and secondInteger > thirdInteger:
    largest = secondInteger
if thirdInteger > firstInteger and thirdInteger > secondInteger:
    largest = thirdInteger

print(smallest)
print(largest)

