# Alternate method using accumulation method.
def f(N):
    total = 0
    for x in range(1, N+1):
        if x % 3 == 0:
            total = total + x
    return total

result1 = f(4)
print(result1)

result2 = f(9)
print(result2)