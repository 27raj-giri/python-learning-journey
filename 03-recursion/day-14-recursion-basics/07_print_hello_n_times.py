# Print "Hello" n times

def text(n):
    if n == 0:
        return

    print("Hello")
    text(n-1)

text(9)