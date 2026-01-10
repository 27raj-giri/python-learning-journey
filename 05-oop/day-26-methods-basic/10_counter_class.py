#  Create a Counter class with methods to increment(), decrement(), and reset() a count.

class Counter:
    def __init__ (self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1

    def decrement(self):
        self.count = self.count - 1

    def reset(self):
        self.count = 0

c = Counter()
c.increment()
c.increment()
print(c.count)

c.reset()
print(c.count)