# def main():
#     print("Welcome To Semicolon")

def leap_year(year):
    leap = False
    if year % 4 == 0 and (
        year % 100 == 0 and year % 400 == 0 or year % 100 != 0
    ):
        leap=True
    return leap

#     # a line solution for the same above code
#     # return (year % 4 == 0) and (year % 100 == 0 and year % 400 == 0 or year % 100 != 0)


if __name__ == "__main__":
    # main()
    print("This is cohort 9!")
    year = int(input("Enter year: "))
    print(leap_year(year))


# from bees.ten_ten import tired_class


# tired_class()
