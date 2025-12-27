# Print all odd numbers from 1 to n

def odd(n):
    if n == 0:
        return

    odd(n-1)

    if n % 2 != 0:
        print(n)

num = int(input("Enter Number: "))
odd(num)