
# Complete File03-ex05.py before reading this file.

def is_fizz_buzz(x):
    return x % 3 == 0 or x % 5 == 0

# Previously we use this way to filter.
# numbers = [
#     x
#     for x in range(1,100)
#     if x % 3 == 0 or x % 5 == 0
# ]

numbers = [
    x
    for x in range(1, 100)
    if is_fizz_buzz(x)
]

print(numbers)
print(sum(numbers))