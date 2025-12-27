# Write a function that finds the frequency of each character in a string.

def frequency(word):
    freq = {}

    for char in word:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1
    
    return freq

text = "Hello"
print(frequency(text))