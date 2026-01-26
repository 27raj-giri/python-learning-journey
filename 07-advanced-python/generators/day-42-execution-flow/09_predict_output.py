def demo():
    print("A")
    yield 1 
    print("B")
    yield 2
    print("C")

gen = demo()

print(next(gen))  
print(next(gen))  
print(next(gen))  