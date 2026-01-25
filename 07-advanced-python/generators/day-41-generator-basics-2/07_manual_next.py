def simple_gen():
    yield "a"
    yield "b"
    yield "c"

gen = simple_gen()

print(next(gen))
print(next(gen))
print(next(gen))