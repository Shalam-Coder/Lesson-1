'''
3.0 Objective: Determine if a given year is a leap year and find all leap years within a user-defined range.

Instructions:

Prompt the user to input a year.
Use conditional statements to check if the year is a leap year:
A year is a leap year if it is divisible by 4 but not by 100, except if it is also divisible by 400.
'''

4000

leapYr = input("Enter a year:\n")
leapYr = int(leapYr)
if (leapYr % 4 == 0 and leapYr % 100 != 0) or (leapYr % 400 == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")