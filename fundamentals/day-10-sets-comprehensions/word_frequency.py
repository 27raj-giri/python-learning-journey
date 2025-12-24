sentence = "Aayush Raj Giri is Raj Giri"
words = sentence.split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

