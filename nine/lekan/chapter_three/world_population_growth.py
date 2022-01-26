import math

population_of_the_world = 7900000000
growth_rate = 1.8
year = 1
future_population = 0
increase_in_population = 0

print('\tYear\t\t World Population \t\t\t Increase ')

for i in range(100):
    future_population = population_of_the_world * math.pow(1+growth_rate, i)

    increase_in_population = future_population - population_of_the_world

    print(f'{i :>8}\t {future_population : >20} \t\t{increase_in_population :>20}')