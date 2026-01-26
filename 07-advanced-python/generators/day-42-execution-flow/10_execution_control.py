def heavy_task():
    print("Doing heavy task...")
    yield 100

my_gen = heavy_task()
print("Generator created Did code run? No.")

print(next(my_gen))