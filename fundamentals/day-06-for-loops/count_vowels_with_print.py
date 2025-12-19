vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text = input("Enter a string: ")
count = 0

for char in text:
    if char in vowels:
        count += 1
        print(char)
    
print(count)
