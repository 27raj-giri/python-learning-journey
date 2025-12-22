nums = [1, 2, 3, 3, 4, 4, 4, 5]
counts = {}
duplicates = []

for num in nums:
    counts[num] = counts.get(num, -0) + 1

for num, count in counts.items():
    if count > 1:
        duplicates.append(num)

print(duplicates)
