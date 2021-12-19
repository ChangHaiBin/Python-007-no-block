
# Complete File03-ex05.py before reading this file.

# Some culture thinks 4, 13, 17, 666 are unlucky numbers.
def is_lucky(x):
    return x != 4 and x != 13 and x != 17 and x != 666

# Previously we use this way to filter.
# numbers = [
#     x
#     for x in range(1,100)
#     if x != 4 and x != 13 and x != 17 and x != 666
# ]

numbers = [
    x
    for x in range(1, 1000)
    if is_lucky(x)
]

print(numbers)
print(sum(numbers))