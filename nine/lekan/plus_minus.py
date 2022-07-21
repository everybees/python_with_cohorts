arr = [1, 1, 0, -1, -1]


def plus_minus(arr):
    count = 0
    negative_count = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
        elif arr[i] < 0:
            negative_count += 1
        elif arr[i] == 0:
            zero += 1

    print(f'{count / len(arr):.6f}')
    print(f'{negative_count / len(arr):6f}')
    print(f'{zero / len(arr):6f}')


plus_minus(arr)
