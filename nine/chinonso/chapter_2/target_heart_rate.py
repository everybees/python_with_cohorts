age = int(input('Enter your age:'))
max_rate = 220 - age
range1 = max_rate * 0.5
range2 = max_rate * 0.85
print('Your Maximum heart rate is ',max_rate,'bpm')
print('The range of your target heart rate is between ',range1,'and',range2,'bpm')