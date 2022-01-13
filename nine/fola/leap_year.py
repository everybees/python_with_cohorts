for i in range(5):
    print("Please enter a given year: ")
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")


# for i in range(5):
#     print("Please enter a given year: ")
#     year = int(input())
#     if year % 4 == 0:
#         if year % 100 != 0:
#             print("This is a leap year")
#     elif year % 400 == 0:
#         print("This is a leap year")
#     else:
#         print("This is not a leap year")
