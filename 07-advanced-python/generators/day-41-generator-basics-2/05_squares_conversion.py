# def squares(n):
  # return [i*i for i in range(1, n+1)] 

def squares(n):
    for i in range(1, n+1):
        yield i * i

for s in squares(5):
    print(s)