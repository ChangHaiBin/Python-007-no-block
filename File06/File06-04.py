
def count_even_numbers(xs):
    even_numbers = [
        x
        for x in xs
        if x % 2 == 0
    ]
    return len(even_numbers)

result1 = count_even_numbers(range(1, 9))
print(result1)

result2 = count_even_numbers([1, 3, 5, 7, 9, 11, 13, 15])
print(result2)

result3 = count_even_numbers([2, 2, 2, 2, 2, 4, 4, 4, 4, 4])
print(result3)