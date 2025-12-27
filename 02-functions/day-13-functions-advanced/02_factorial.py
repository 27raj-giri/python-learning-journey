def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        if n == 0 or n ==1:
            return 1
        else:
            fact = fact * i
    return fact

num = int(input("Enter number: "))
print("Factorial of", num, "is:", factorial(num))
