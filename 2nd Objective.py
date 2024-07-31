'''
2.0 Objective: Write a Python program that checks whether a given number is even or odd and whether it is also positive, negative, or zero.

Instructions:

Prompt the user to input a number.
Use nested if-else statements to determine if the number is even or odd, and whether it is positive, negative, or zero.
Print both results.
'''

varX = input("Enter a number:\n")
varX = int(varX)

if varX == 0:
    print("THe number is 0")

#nesting conditions

elif varX > 0:
    if varX % 2 == 0:
        print("The number is positive")
        print("The number is even")
    else:
        print("The number is positive")
        print("THe number is odd")

elif varX < 0:
    if varX % 2 == 0:
        print("The number is even")
        print("The number is negative")
    else:
        print("The number is odd")
        print("The number is negative")

