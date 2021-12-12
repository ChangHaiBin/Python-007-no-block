
# Create a function "f" that takes in two integers "a", "b"
# Find the sum of all numbers "x" between "a" and "b" (both inclusive)
#
# Hint:
# 1. There are two cases: a <= b, or   a > b
# 2. If a < b, then range(a, b+1) will list down all integers from a to b (but will not include "b+1")
#    which you can "sum" afterwards.

def f(a, b):
    # .................
    return 1000


print(f(1, 5))      # Answer: 15
print(f(5, 1))      # Answer: 15
print(f(20, 20))    # Answer: 20
print(f(1, 100))    # Answer: 5050
print(f(10, 20))    # Answer: 165
print(f(20, 10))    # Answer: 165
