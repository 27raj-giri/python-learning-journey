def sub_gen():
    yield "A"
    yield "B"

def main_gen():
    yield from sub_gen()
    yield "C"

for x in main_gen():
    print(x)