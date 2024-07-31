password = input("Password:\n")

length = len(password)

if length <= 6:
    print(length, "is weak")
elif 6 < length < 9:
    print(length, "is moderate")
else:
    print(length, "is strong")