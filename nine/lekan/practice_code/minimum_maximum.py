import sys


def max_min(arr):
    max = -sys.maxsize - 1
    min = sys.maxsize
    sum = 0
    for x in range(len(arr)):
        sum += x
        if x > max:
            max = x
        if x < min:
            min = x
    print(sum - max, sum - min)
