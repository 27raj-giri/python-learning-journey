# Print all even numbers from n to 1

def even(n):
    if n == 1:
        return

    if n % 2 == 0:
        print(n)

    even(n-1)

num = int(input("Enter Number: "))
even(num)