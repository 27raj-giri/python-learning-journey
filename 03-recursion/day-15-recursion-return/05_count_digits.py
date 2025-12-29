# Count number of digits

def count(n):
    if n < 10:
        return 1

    return 1 + count(n // 10)

print(count(123))