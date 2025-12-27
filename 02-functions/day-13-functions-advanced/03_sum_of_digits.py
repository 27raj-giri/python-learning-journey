# Write a function that returns the sum of digits of a number.

def sum(n):
    total = 0

    for digits in str(n):
        total = total + int(digits)

    return total

number = int(input("Enter number: "))
print(sum(number))