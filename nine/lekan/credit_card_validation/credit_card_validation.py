def isvalid(account_number):
    card_is_valid = (13 <= account_number.length() <= 16
                     ) and (digits.prefix(4) or digits.startsWith("5") or digits.startsWith(
        "37") or digits.startsWith("6")) and ((sumOfDoubleEvenNumber(digits) + sumOfOddNumber(digits)) % 10
                                              == 0)

    return card_is_valid


def sum_of_double_even_place(number):
    sum = 0
    for i in range(number.length - 2, 0, -2):
        sum += get_digit(int(number.charAt(i)) * 2)
    return sum


def get_digit(num):
    number_is_less_than_nine = num < 9
    if numberIsLessThanNine:
        return num
    else:
        return (num / 10) + (num % 10)


def sum_of_odd_place_number(number):
    sum = 0
    for i in range(number.length -1, 0, -2):
        sum += int(number.charAt(i) + " ")
    return sum


def prefix_matched(number, prefix):
    prefix = ("4", "5", "37", "6")

    if number.startswith(prefix):
        return true
    else:
        return false


def get_size(d):
    return d.len()

