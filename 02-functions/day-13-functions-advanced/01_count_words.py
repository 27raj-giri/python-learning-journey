# Write a function that returns the number of words in a sentence.

def count(words):
    result = words.split()

    return len(result)     

sentence = "Aayush Raj Giri"
print(count(sentence))

