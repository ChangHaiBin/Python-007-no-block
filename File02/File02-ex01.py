
# Complete the function below, that calculates:
#     the price of a basket of goods after discount
#     if original_price < $50, no discount
#     if $50 <= original_price < $100, apply a 5% discount
#     if $100 <= original_price, apply a 10% discount.
def apply_discount(original_price):
    ....................

basket1 = 49
final_price1 = apply_discount(basket1)
print(f"The final price of Basket 1 is {final_price1}")

basket2 = 80
final_price2 = apply_discount(basket2)
print(f"The final price of Basket 2 is {final_price2}")

basket3 = 500
final_price3 = apply_discount(basket3)
print(f"The final price of Basket 3 is {final_price3}")