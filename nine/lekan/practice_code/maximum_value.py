def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3

    return max_value


def main():
    value1 = 23
    value2 = 45
    value3 = 20
    max_value = maximum(value1, value2, value3)
    print('The maximum value is ', max_value)


main()
