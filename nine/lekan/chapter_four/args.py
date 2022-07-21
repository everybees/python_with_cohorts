def average(*args):
    return sum(args) / len(args)


print(average(2, 3, 4))


def calculate_product(*args):
    product = 1
    for values in args:
        product *= values
    return product


print(calculate_product(10, 20, 30))

s = 3 / 2

print(s)
