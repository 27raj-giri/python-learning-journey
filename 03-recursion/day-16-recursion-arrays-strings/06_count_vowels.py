# Count vowels in a string

def count(text, idx = 0):
    if idx == len(text):
        return 0

    vowel = 0
    if text[idx] in 'aeiouAEIOU':
        vowel = 1

    return vowel + count(text, idx + 1)

print(count("Aayush"))