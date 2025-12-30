text = "swiss"
counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

for char in text:
    if counts[char] == 1:
        print(f"The first non-repeating character is '{char}'")
        break