'''
Write a program that works out whether if a given year
is a leap year. A normal year has 365 days, leap years
have 366, with an extra day in February.
'''

year: int = int(input("Which year do you want to check? "))
leap: bool = False

if year % 4 == 0:
    leap = True
if year % 100 == 0:
    leap = False
if year % 400 == 0:
    leap = True

if leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is a normal year.")
