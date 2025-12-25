def convert(c):
    f = (c * 9/5) + 32
    return f

celcius = int(input("Enter degree in Celcius: "))
print(convert(celcius))