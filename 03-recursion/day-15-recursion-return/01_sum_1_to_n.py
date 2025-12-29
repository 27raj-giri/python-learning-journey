# Find sum of numbers from 1 to n

def sum(n):
    if(n == 0):
        return 0
        
    return sum(n-1) + n

num = int(input("Enter Number: "))
print(sum(num))
