# (What Does This Code Do?) What does the following program print?
# for row in range(10):
# for column in range(10):
# print('<' if row % 2 == 1 else '>', end='')
# print()


for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
        print()
