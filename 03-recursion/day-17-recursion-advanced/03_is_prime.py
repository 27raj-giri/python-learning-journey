# Check if a number is prime (Recursively)

def prime(n, i=2):

    if n <= 1: return False
    if n == i: return True
    if n % i == 0: return False

    return prime(n, i+1)

print(prime(7))