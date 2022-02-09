print("Hypotenuse\t\t", "Side A\t\t", "Side B")
for i in range (1, 20):
    for j in range (1, 20):
        for k in range (1, 20):
            a  = ((j **2) + (k** 2))
            if (i ** 2) == a :
                print (i,"\t\t\t", j,"\t\t", k)
            #  print("This is a pythagorean triple")
            # else:
            #     print("This is not a pythagorean triple")

