
def product(numbers):
    subtotal = 1
    for number in numbers:
        subtotal = subtotal * number
    return subtotal

result = product(range(1, 10))
print(result)