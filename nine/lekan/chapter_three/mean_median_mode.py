import statistics

user_input = [9, 11, 22, 34, 34, 17, 22, 34, 22, 40]

mean = sum(user_input)/len(user_input)

print('The mean is ', mean)

mode = statistics.mode(user_input)
print('The mode is ', mode)

median = statistics.median(user_input)
print('The median is ', median)
