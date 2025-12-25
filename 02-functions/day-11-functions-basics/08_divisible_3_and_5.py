def divisible(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Divisible by both 3 and 5"
    else:
        return "Not divisible by both 3 and 5"

num = int(input("Enter number: "))
print(divisible(num))
