# 3.28 (Intro to Data Science: Mean, Median and Mode) Calculate the mean, median and
# mode of the values 9, 11, 22, 34, 17, 22, 34, 22 and 40. Suppose the values included another 34.
# What problem might occur?

import statistics


# frequency = 0
# mode = 0

from statistics import mean

# total = 0
numbers = [9, 11, 17, 22, 22, 22, 34, 34, 40]
# for i in range(9):
#     total += numbers[i]

    # if mode == numbers[i] or mode != numbers[i]:
    #     if numbers[0] == 0:
    #         mode = numbers[1]
    #         frequency += 0
    #     elif numbers[0] != 0:
    #         mode = numbers[1]
    #         frequency += 0
    # if mode == numbers[i]:
    #     mode = numbers[i]
    #     frequency += 1



# if len(numbers) % 2 == 1:
#     print(numbers[(len(numbers)-1) // 2])
# elif len(numbers) % 2 == 0:
#     median = numbers[len(numbers) // 2] + numbers[(len(numbers) // 2)-1]
#     print(median / 2)
#
# mean = total / len(numbers)
# print(f"The mean is {mean:.2f}")


print(f"The mean of the numbers is {statistics.mean(numbers):.2f}")
print(f"The median value of the numbers is {statistics.median(sorted(numbers))}")
print(f"The number with the highest frequency is {statistics.mode(sorted(numbers))}")


