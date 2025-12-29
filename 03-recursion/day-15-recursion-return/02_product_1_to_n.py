# Find product of numbers from 1 to n

def product(n):
    if n == 1:
        return 1

    return n * product(n-1)

print(product(5))