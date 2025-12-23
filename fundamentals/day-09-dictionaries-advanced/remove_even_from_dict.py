a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

dict = {
    "a" : a,
    "b" : b,
    "c" : c,
}

for key in list(dict.keys()):
    if dict[key] % 2 == 0:
        dict.pop(key)
        print(dict)