
# Complete File03-ex05.py before reading this file.

def is_odd(x):
    if x % 2 == 1:
        return True
    else:
        return False

# Previously we use this way to filter.
# numbers = [
#     x
#     for x in range(1,100)
#     if x % 2 == 0
# ]

numbers = [
    x
    for x in range(1, 100)
    if is_odd(x)
]

print(numbers)
print(sum(numbers))