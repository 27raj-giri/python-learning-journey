def lazy_squares(n):
    for i in range(1, n+1):
        print(f"Calculating square of {i}")
        yield i * i

gen = lazy_squares(5)

print("Generator created. Calculation hasn't started yet.")
print("Give me one:", next(gen))
print("Give me another:", next(gen))