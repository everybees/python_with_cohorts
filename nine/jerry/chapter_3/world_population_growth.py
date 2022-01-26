# 3.27 (World Population Growth) World population has grown considerably over the
# centuries. Continued growth could eventually challenge the limits of breathable air,
# drinkable water, arable land and other limited resources. There’s evidence that growth has been
# slowing in recent years and that world population could peak some time this century, then
# start to decline.
# For this exercise, research world population growth issues. This is a controversial
# topic, so be sure to investigate various viewpoints. Get estimates for the current world
# population and its growth rate. Write a script that calculates world population growth
# each year for the next 100 years, using the simplifying assumption that the current growth
# rate will stay constant. Print the results in a table. The first column should display the year
# from 1 to 100. The second column should display the anticipated world population at
# the end of that year. The third column should display the numerical increase in the world
# population that would occur that year. Using your results, determine the years in which
# the population would be double and eventually quadruple what it is today.


current_world_population = 7921322903
world_population_growth_rate = 0.0105
print("YEAR\tNEW_WORLD_POPULATION\tESTIMATED_POPULATION_INCREASE")
for i in range(1, 101):
    estimated_population_increase = current_world_population * world_population_growth_rate
    new_world_population = current_world_population + estimated_population_increase
    print("Year", i, end="\t")
    print(f"{new_world_population:.2f}", end="\t\t\t")
    print(f"{estimated_population_increase:.2f}", end="\t")
    current_world_population += estimated_population_increase
    print()