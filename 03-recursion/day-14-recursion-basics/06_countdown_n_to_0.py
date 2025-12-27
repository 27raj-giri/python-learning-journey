# Count down from n to 0

def countdown(n):
    if n == 0:
        print(n)
        return
    
    print(n)
    countdown(n-1)

countdown(10)