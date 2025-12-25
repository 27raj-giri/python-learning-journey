# Write a function that counts vowels in a string.

def count(v):
    count = 0
    for char in text:
        if char in v:
            count = count + 1

    return count

text = "Aayush Raj Giri"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

print(count(vowels))
    