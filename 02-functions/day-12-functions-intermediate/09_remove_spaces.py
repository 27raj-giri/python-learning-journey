# Write a function that removes spaces from a string.

def remove(text):
    return text.replace(" ", "")
    
sentence = "Aayush Raj Giri"
result = remove(sentence)

print(result)