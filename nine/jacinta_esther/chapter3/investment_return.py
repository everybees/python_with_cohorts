count = 1
for i in range(0, 30):
    amount = 1000 * ((1.0 + 0.07) ** i)
    print("The investment return after", count, "years is: ", amount)
    count += 1
