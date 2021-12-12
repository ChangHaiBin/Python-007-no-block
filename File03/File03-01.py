def f(N):
    numbers = [
        x
        for x in range(1, N+1)
        if x % 3 == 0
    ]
    return sum(numbers)

result1 = f(4)
print(result1)

result2 = f(9)
print(result2)


# Remark: You can even add a "print" statement in the function, to print out the numbers that you want to sum.
