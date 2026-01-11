# Create a StringManipulator class with methods: reverse(), uppercase(), word_count().

class StringManipulator:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]
    
    def uppercase(self):
        return self.text.upper()
    
    def word_count(self):
        words = self.text.split()
        return len(words)

s = StringManipulator("Aayush Raj Giri")
print(s.reverse())
print(s.word_count())
print(s.uppercase())
    