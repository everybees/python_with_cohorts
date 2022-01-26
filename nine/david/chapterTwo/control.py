my_var = 0
if my_var % 2:
    if my_var**3 != 27:
        my_var = my_var + 4
    else:
        my_var /= 1.5
else:
    my_var -= 2
print(my_var)