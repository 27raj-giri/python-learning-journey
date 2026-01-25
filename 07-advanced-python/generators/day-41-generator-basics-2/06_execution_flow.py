def mixed_bag():
    yield "Start"
    yield 1
    yield 2
    yield "End"

for item in mixed_bag():
    print(item)