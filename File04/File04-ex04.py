
# What's wrong with the following code?
def calculate_total(order, amount):
    if order == "BURGER":
        print("Each burger costs $7")
        return amount * 7

    elif order == "PIZZA":
        print("Each pizza costs $8")
        return amount * 8

    else:
        print("I don't understand your order.")
        return 0

# I want to order 10 burgers, which I expect the final total to be $70
# What's wrong?
total_amount = calculate_total(10, "BURGER")
print(f"The final amount is ${total_amount}")
