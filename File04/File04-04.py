
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

process_order(order="BURGER",
              payment=20)

print("=====================")

process_order(payment=10,
              order="PIZZA")