a = [1, 2, 3]
b = [3, 2, 1]


def compare(c, d):
    a_point = 0
    b_point = 0
    for i in range(len(c)):
        if c[i] > d[i]:
            a_point += 1
        elif c[i] == d[i]:
            a_point += 0
            b_point += 0
        else:
            b_point += 1
    return [a_point, b_point]


print(compare(a, b))
