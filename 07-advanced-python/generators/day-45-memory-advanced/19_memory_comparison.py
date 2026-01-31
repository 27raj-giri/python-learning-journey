import sys

list_data = [i for i in range(10000)]
gen_data = (i for i in range(10000))

print(f"List memory: {sys.getsizeof(list_data)} bytes")
print(f"Generator memory: {sys.getsizeof(gen_data)} bytes")