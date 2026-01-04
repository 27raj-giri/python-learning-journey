# Find the most frequent word (Interview Favorite)

word_count = {}

with open("data.txt", "r") as f:
    words = f.read().split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_frequent = max(word_count, key=word_count.get)

print(most_frequent)