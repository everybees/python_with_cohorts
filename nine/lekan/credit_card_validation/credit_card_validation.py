def isvalid(account_number):
    card_is_valid = (13 <= len(account_number) <= 16
                     ) and (account_number.startswith("4") or account_number.startsWith(
        "5") or account_number.startsWith(
        "37") or account_number.startsWith("6")) and ((sum_of_double_even_place(account_number) +
                                                       sum_of_odd_place_number(account_number)) % 10
                                                      == 0)

    return card_is_valid


def sum_of_double_even_place(number):
    sum = 0
    for i in range(len(number) - 2, 0, -2):
        sum += get_digit(int(number[i]) * 2)
    return sum


def get_digit(num):
    number_is_less_than_nine = num < 9
    if number_is_less_than_nine:
        return num
    else:
        return (num // 10) + (num % 10)


def sum_of_odd_place_number(number):
    sum = 0
    for i in range(len(number) - 1, 0, -1):
        sum += int(number[i] + " ")
    return sum


def prefix_matched(number, prefix):
    prefix = ("4", "5", "37", "6")

    if number.startswith(prefix):
        return True
    else:
        return False


def get_size(d):
    return d.len()


print(isvalid("4388576018410707"))
