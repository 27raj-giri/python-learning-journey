# Print first n natural numbers

def natural_num(n):
    if n == 0:
        return
    
    natural_num(n-1)
    print(n)

natural_num(50)