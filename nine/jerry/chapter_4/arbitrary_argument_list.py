# 4.13 (Arbitrary Argument List) Calculate the product of a series of integers that are
# passed to the function product, which receives an arbitrary argument list.
# Test your function with several calls, each with a different number of arguments.


def product(*args):
    value = 1
    for i in range(len(args)):
        value *= args[i]
    return value


print(product(77, 8))
