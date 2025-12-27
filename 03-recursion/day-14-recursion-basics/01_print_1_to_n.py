# Print numbers from 1 to n

def one2n(n):
    if n == 0:
        return

    one2n(n-1)
    print(n)

one2n(50)