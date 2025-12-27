# Print numbers from n to 1

def n2one(n):
    if n == 0:
        return

    print(n)
    n2one(n-1)

n2one(100)     