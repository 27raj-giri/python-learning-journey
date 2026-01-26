def tracker():
    print("Start of generator")
    yield 1
    print("Middle of generator")
    yield 2
    print("End of generator")

g = tracker()

print("Caller asks for 1:")
print(next(g))

print("\nCaller asks for 2:")
print(next(g))
