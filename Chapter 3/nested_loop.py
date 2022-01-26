# 3.17 (Nested Loops) Write a script that displays the following triangle patterns separately, one below the other.
# Separate each pattern from the next by one blank line. Use for
# loops to generate the patterns. Display all asterisks (*) with a single statement of the form
# print('*', end='')
# which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
# each line with zero or more space characters.


for serial_n in range(0, 11, 1):
    for content in range(1, serial_n, 1):
        print("* ", end=" ")
    print()
print()

for serial_n in range(11, 0, -1):
    for content in range(1, serial_n, 1):
        print("* ", end=" ")
    print()
print()

for serial_n in range(0, 11, 1):
    for content in range(0, serial_n, 1):
        print("  ", end=" ")
    for content in range(11, serial_n, -1): #Start from 11 at the top and come down for serial_n as serial_n goes up
        print("* ", end=" ")
    print()
print()

for serial_n in range(11, 0, -1):
    for content in range(1, serial_n, 1):
        print("  ", end=" ")
    for content in range(11, serial_n, -1): #Start from 11 at the bottom and come up for serial_n as serial_n goes down
        print("* ", end=" ")
    print()
print()


for serial_n in range(5, 0, -1):
    for content in range(0, serial_n, 1):
        print("  ", end=" ")
    for content in range(4, serial_n, -1): # Start from 11 at the bottom and come up for serial_n as serial_n goes down
        print("* ", end=" ")
    for x_content in range(serial_n, 5, 1):
        print("* ", end=" ")
    print()

for serial_n in range(0, 5, 1):
    for content in range(0, serial_n, 1):
        print("  ", end=" ")
    for content in range(4, serial_n, -1): # Start from 11 at the top and come down for serial_n as serial_n goes up
        print("* ", end=" ")
    for x_content in range(4, serial_n, -1):
        print("* ", end=" ")
    print()
print()