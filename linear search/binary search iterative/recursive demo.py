'''
1. factorial(0) = 1  Non Recursive
2. factorial(n) = n* factorial(n-1) Recursive
'''


def multiply(m, n):
    if n == 0 or m == 0:
        return 0
    return m+multiply(m, n-1)


print(multiply(2, 3))
