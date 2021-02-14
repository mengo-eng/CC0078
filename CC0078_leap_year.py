# Assignment - 007/8 (Leap Year) - Check whether a given year is a leap year.
# C7185-Elnur
year = int(input("Enter a year to check whether it is a leap year: "))
if year % 4 ==0:
    if year % 100 == 0 and year % 400 != 0:
        print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")