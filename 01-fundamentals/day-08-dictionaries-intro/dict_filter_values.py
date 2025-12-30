a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

dict = {
    "a" : a,
    "b" : b,
    "c" : c,
}

num = int(input("Enter number: "))

for value in dict.values():
    if value > num:
        print(value)