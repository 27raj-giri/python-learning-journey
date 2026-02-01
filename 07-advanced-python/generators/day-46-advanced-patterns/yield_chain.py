def sub_gen():
    yield 1 
    yield 2

def main_gen():
    for num in sub_gen():
        yield num
    yield 3

for x in main_gen():
    print(x)