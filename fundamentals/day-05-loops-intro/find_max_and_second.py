num = [27, 9, 18, 36, 7]
result = max(num)
print("Max = ", result)

num.sort()
second_largest = num[-2]
print("SecondMax =", second_largest)

result = num.pop(-2)
print("Numbers without second max = ", num)