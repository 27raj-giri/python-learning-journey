# Write a function that checks if a string is a palindrome.

def check(text):
    if text == text[::-1]:
        return True
    else:
        return False

word = input("Enter text: ")

if check(word):
    print("Palindrome")
else:
    print("Not a palindrome")