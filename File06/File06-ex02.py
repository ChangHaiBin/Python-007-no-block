
# Create a function below, that accepts a list of numbers "xs"
# and count how many "special" numbers that are
# divisible by 3   OR   divisible by 5
def count_special_numbers(xs):
    # ...............
    return 0

result1 = count_special_numbers(range(1, 16))
print(result1)    # Answer: 7

result2 = count_special_numbers([1, 2, 4, 7, 8, 11, 13, 14])
print(result2)    # Answer: 0

result3 = count_special_numbers([3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 12, 12, 12, 12, 12, 15, 15, 15, 15, 15])
print(result3)    # Answer: 20