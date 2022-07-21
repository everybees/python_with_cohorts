def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y


value = [1, 2, 3, 4, 5]
print(mystery(value))

