text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count = count + 1

print("Number of Vowels:", count)