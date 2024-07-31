'''
5.0 Objective: Calculate the final price after applying multiple discounts based on the initial price and membership status.

Instructions:

Prompt the user to input the initial price of an item.
Prompt the user to input their membership status (Gold, Silver, or None).
Apply discounts based on the following rules:
If the initial price is greater than $100, apply a 10% discount.
Additionally, if the user is a Gold member, apply an extra 5% discount. # 5/100
If the user is a Silver member, apply an extra 2% discount.
Calculate and print the final price.
'''

price = input("What is the price of the item?\n")
price = float(price)

membership = input("Membership Status?\n")
membership = membership.lower()

discount = 0

if price > 100:
    if membership == "gold":
        discount = 0.15 * price
    elif membership == "silver":
        discount = 0.12 * price
    else:
        discount = 0.01 * price

newPrice = price - discount
print(newPrice, ": Total after discount")
