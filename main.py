'''1.0 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.'''


while True:

    gradeScore = input("Enter a score between 0.0 - 1.0\n ")
    gradeScore = float(gradeScore)

    if gradeScore > 1.0:
        print("Error: The score entered does not match range")
        quit()
    elif gradeScore >= 0.9:
        print("A")
    elif gradeScore >= 0.8:
        print("B")
    elif gradeScore >= 0.7:
        print("C")
    elif gradeScore >= 0.6:
        print("D")
    elif gradeScore < 0.6:
        print("F")

