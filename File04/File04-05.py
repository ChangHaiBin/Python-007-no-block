
def process_order(order, payment):
    if order == "BURGER":
        print(f"A burger costs $7. You have made a payment of {payment}")
        change = payment - 7
        print(f"Your change is ${change}")

    elif order == "PIZZA":
        print(f"A Pizza costs $8. You have made a payment of {payment}")
        change = payment - 8
        print(f"Your change is ${change}")

    else:
        print("I do not understand your order.")
        print(f"Order: {order}")
        print(f"Payment: {payment}")

# Here, we messed up the "order" with "payment"!
# It leads to error in the code!

# In some other language (type checked language), this will never happen.
# Because you cannot input an INTEGER into a STRING/WORD field.
process_order(20, "BURGER")
