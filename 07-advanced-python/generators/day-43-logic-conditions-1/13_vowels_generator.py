def vowels(text):
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            yield char

for v in vowels("Aayush Raj Giri"):
    print(v)