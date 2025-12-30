set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = []

for num in set1:
    if num in set2:
        intersection.append(num)

print(intersection)
