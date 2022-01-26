


numerator=4
denominator=1

pi_value=0
divisor=3
print("one term"+"\t"+"two terms"+"\t"+"three terms")

for number in  range(200_000):

    if number % 2==1:
         pi_value  +=  - (numerator / denominator) 

    else:
        pi_value += (numerator / denominator)
    denominator +=2
    print("pi is ",pi_value)

print(f"Final value of pi is {pi_value:>.5f}")
