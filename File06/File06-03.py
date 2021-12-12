
# Just like the plural form of "number" is "numbers"
# We call a list of "x" as "xs"
def product(xs):
    subtotal = 1
    for x in xs:
        subtotal = subtotal * x
    return subtotal

result = product(range(1, 10))
print(result)