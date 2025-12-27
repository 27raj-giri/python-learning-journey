# Write a function that checks if a number is prime.

def check(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

number = int(input("Enter number: "))
print(check(number))
