def fahrenheit(celsius):
    return (9 / 5) * celsius + 32


print('Celsius\t\tFahrenheit')
for i in range(101):

    print(i, '\t\t\t\t', fahrenheit(i))
