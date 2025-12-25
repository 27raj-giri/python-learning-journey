def result(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

num = int(input("Enter a number: "))
print("The number is", result(num))
