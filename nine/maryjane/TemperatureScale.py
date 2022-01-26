# celsius= input("enter value of celsius")
# celsius= int (celsius)
# fahrenheit=32+((9*celsius)/5)
# print(fahrenheit)



def temp_scale(celsius):
    for celsius in range(1, 32):
        fahrenheit=((9*celsius)/5)+32
        print("%f"%fahrenheit)
temp_scale(1)