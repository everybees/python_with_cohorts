# Author: Joshua
# Title : comparing between arrays
names = ["Samuel", "Chukwueze", "Makinwa", "macus", "john", "Zoe", "Legend" ]
cars = ["Volvo", "Tesla", "Mazda", "Mercedes-Benz", "Limousine", " SUVs", "Sedans"]

count = -1
name_maximum = 0
cars_maximum = 0
name = names[count]
car = cars[count]

cars_minimum = 10000
names_minimum = 10000
# names_of_five = " "

while count < len(names)-1:
    count = count + 1
    if len(names[count]) > name_maximum:
        name_maximum = len(names[count])
        name = names[count]

    if len(cars[count]) > cars_maximum:
        cars_maximum = len(cars[count])
        car = cars[count]

    if len(names[count]) < names_minimum:
        names_minimum = len(names[count])
        name_name = names[count]

    if len(cars[count]) < cars_minimum:
        cars_minimum = len(cars[count])
        car_name = cars[count]


if cars_maximum > name_maximum:
    print("The highest length is {},{}".format(cars_maximum, car))
else:
    print("The highest length is {},{}".format(name_maximum, name))

if cars_minimum < names_minimum:
    print("The Lowest length is {},{}".format(cars_minimum, car_name))
else:
    print("The Lowest length is {},{}".format(names_minimum, name_name))
