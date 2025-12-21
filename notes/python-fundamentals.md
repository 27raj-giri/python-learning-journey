# 📚 PYTHON LEARNING NOTES - COMPLETE REFERENCE
## Days 1-17 | 129 Programs | December 2025

---

## 📋 TABLE OF CONTENTS

1. [Fundamentals (Days 1-10)](#fundamentals)
2. [Functions (Days 11-13)](#functions)
3. [Recursion (Days 14-17)](#recursion)
4. [Quick Reference Patterns](#patterns)
5. [Common Mistakes to Avoid](#mistakes)

---

<a name="fundamentals"></a>
## 📘 PART 1: FUNDAMENTALS (DAYS 1-10)

### **DAY 1-2: Variables, Input, Conditionals**

#### Variables & Data Types
```python
# Integer
age = 21

# Float
price = 99.99

# String
name = "Aayush"

# Boolean
is_active = True
```

#### Type Casting
```python
num = int("10")        # String to int
price = float("9.99")  # String to float
text = str(100)        # Int to string
```

#### User Input
```python
name = input("Enter name: ")           # Always returns string
age = int(input("Enter age: "))        # Convert to int
price = float(input("Enter price: "))  # Convert to float
```

#### Conditionals
```python
# If-else
if condition:
    # code
else:
    # code

# If-elif-else
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Comparison operators
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal
<=  # Less than or equal

# Logical operators
and  # Both conditions true
or   # At least one true
not  # Negation
```

#### Common Patterns
```python
# Even/Odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Divisibility
if num % 5 == 0:
    print("Divisible by 5")

# Range check
if 18 <= age <= 65:
    print("Working age")
```

---

### **DAY 3-4: Strings & Lists**

#### String Methods
```python
text = "Hello World"

text.upper()          # "HELLO WORLD"
text.lower()          # "hello world"
text.replace("H", "h") # "hello World"
text.split()          # ["Hello", "World"]
text.split(",")       # Split by comma
" ".join(["a", "b"])  # "a b"

len(text)             # Length
text[0]               # First character
text[-1]              # Last character
text[0:5]             # Slicing
```

#### String Formatting
```python
name = "Aayush"
age = 21

# f-strings (best)
print(f"My name is {name}, age {age}")

# format()
print("My name is {}, age {}".format(name, age))

# Concatenation
print("Name: " + name)
```

#### Lists
```python
numbers = [1, 2, 3, 4, 5]

# Accessing
numbers[0]            # First element: 1
numbers[-1]           # Last element: 5
numbers[1:4]          # Slicing: [2, 3, 4]

# Methods
numbers.append(6)     # Add to end
numbers.insert(0, 0)  # Insert at index
numbers.pop()         # Remove last
numbers.pop(0)        # Remove at index
numbers.remove(3)     # Remove value
numbers.reverse()     # Reverse in-place
numbers.sort()        # Sort in-place

# Other operations
len(numbers)          # Length
max(numbers)          # Maximum
min(numbers)          # Minimum
sum(numbers)          # Sum
```

#### Tuples (Immutable Lists)
```python
coords = (10, 20)

# Accessing (same as lists)
coords[0]             # 10

# Cannot modify!
# coords[0] = 5       # ERROR!

# Workaround
temp = list(coords)   # Convert to list
temp[0] = 5           # Modify
coords = tuple(temp)  # Convert back
```

---

### **DAY 5-7: Loops**

#### For Loops
```python
# Loop with range
for i in range(5):
    print(i)  # 0 1 2 3 4

# Range with start and stop
for i in range(1, 6):
    print(i)  # 1 2 3 4 5

# Range with step
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

# Reverse
for i in range(10, 0, -1):
    print(i)  # 10 9 8 ... 1

# Loop over list
names = ["A", "B", "C"]
for name in names:
    print(name)

# Loop over string
for char in "hello":
    print(char)
```

#### While Loops
```python
# Basic while
i = 0
while i < 5:
    print(i)
    i += 1

# With condition
num = 10
while num > 0:
    print(num)
    num -= 1

# Infinite loop (use break)
while True:
    answer = input("Continue? (yes/no): ")
    if answer == "no":
        break
```

#### Loop Control
```python
# Break - exit loop
for i in range(10):
    if i == 5:
        break  # Stop at 5

# Continue - skip iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Else with loops (runs if no break)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed")  # This runs
```

#### Common Loop Patterns
```python
# Accumulator (sum)
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55

# Counter
count = 0
for char in "hello":
    if char in "aeiou":
        count += 1

# Finding max
numbers = [3, 7, 2, 9, 1]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

# Building strings
result = ""
for char in "hello":
    result = char + result  # Reverse
```

---

### **DAY 8-9: Dictionaries**

#### Dictionary Basics
```python
# Creation
student = {
    "name": "Aayush",
    "age": 21,
    "city": "Gorakhpur"
}

# Accessing
print(student["name"])         # "Aayush"
print(student.get("name"))     # "Aayush"
print(student.get("grade", 0)) # 0 (default)

# Modifying
student["age"] = 22            # Update
student["grade"] = "A"         # Add new

# Deleting
del student["city"]            # Delete key
student.pop("age")             # Remove and return
```

#### Dictionary Methods
```python
data = {"a": 1, "b": 2, "c": 3}

# Iteration
for key in data:
    print(key)  # Keys only

for value in data.values():
    print(value)  # Values only

for key, value in data.items():
    print(key, value)  # Both

# Useful methods
data.keys()           # All keys
data.values()         # All values
data.items()          # Key-value pairs
"a" in data           # Check key exists
data.clear()          # Remove all
```

#### Counting Pattern with Dictionaries
```python
# Count frequency
text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
# Result: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Group by property
words = ["apple", "banana", "cherry", "date"]
by_length = {}
for word in words:
    length = len(word)
    by_length.setdefault(length, [])
    by_length[length].append(word)
```

#### Dictionary Inversion
```python
# Swap keys and values
original = {1: "a", 2: "b", 3: "c"}
reversed_dict = {}
for key, value in original.items():
    reversed_dict[value] = key
# Result: {'a': 1, 'b': 2, 'c': 3}
```

---

### **DAY 10: Sets & Comprehensions**

#### Sets (Unique Elements)
```python
# Creation
numbers = {1, 2, 3, 4, 5}
numbers = set([1, 2, 2, 3])  # {1, 2, 3}

# Operations
numbers.add(6)        # Add element
numbers.remove(3)     # Remove (error if not found)
numbers.discard(3)    # Remove (no error)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1 | set2           # Union: {1, 2, 3, 4, 5}
set1 & set2           # Intersection: {3}
set1 - set2           # Difference: {1, 2}
set1 ^ set2           # Symmetric diff: {1, 2, 4, 5}
```

#### List Comprehensions
```python
# Basic syntax
[expression for item in iterable]

# Examples
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

upper = [word.upper() for word in ["a", "b", "c"]]
# ['A', 'B', 'C']
```

#### Dictionary Comprehensions
```python
# Basic syntax
{key: value for item in iterable}

# Examples
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

lengths = {word: len(word) for word in ["hi", "hello"]}
# {'hi': 2, 'hello': 5}
```

---

<a name="functions"></a>
## 📗 PART 2: FUNCTIONS (DAYS 11-13)

### **DAY 11-12: Function Basics**

#### Function Definition
```python
# Basic function
def greet():
    print("Hello!")

greet()  # Call function

# With parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Aayush")

# With return
def add(a, b):
    return a + b

result = add(5, 3)  # 8

# Multiple parameters
def calculate(a, b, c):
    return a + b + c

# Default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # "Hello, Guest!"
greet("Aayush")   # "Hello, Aayush!"
```

#### Return vs Print
```python
# Print - just displays
def print_sum(a, b):
    print(a + b)

print_sum(3, 5)  # Displays 8
result = print_sum(3, 5)  # result is None!

# Return - gives back value
def return_sum(a, b):
    return a + b

result = return_sum(3, 5)  # result is 8
print(result * 2)          # Can use it: 16
```

#### Function Patterns
```python
# Boolean return
def is_even(num):
    return num % 2 == 0

# Multiple returns
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Return multiple values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
```

---

### **DAY 13: Advanced Functions**

#### Working with Lists
```python
# Process list
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Find in list
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Filter list
def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
```

#### Working with Strings
```python
# Count characters
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Transform string
def remove_spaces(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result

# Check property
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
```

#### Advanced Algorithms
```python
# Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Prime checker
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Digit operations
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total
```

---

<a name="recursion"></a>
## 📕 PART 3: RECURSION (DAYS 14-17)

### **DAY 14: Print-Based Recursion**

#### Basic Pattern
```python
def recursive_function(n):
    # Base case - when to stop
    if n == 0:
        return
    
    # Recursive case - call with smaller input
    recursive_function(n - 1)
    print(n)
```

#### Ascending Order (Print After)
```python
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)  # Recurse first
    print(n)             # Then print
```

#### Descending Order (Print Before)
```python
def print_n_to_1(n):
    if n == 0:
        return
    print(n)             # Print first
    print_n_to_1(n - 1)  # Then recurse
```

---

### **DAY 15: Return-Based Recursion**

#### The Trust Pattern
```python
return current_value + recursive_call(smaller_problem)
```

#### Sum Pattern
```python
def sum_1_to_n(n):
    if n == 0:
        return 0
    return n + sum_1_to_n(n - 1)
```

#### Factorial Pattern
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

#### Digit Processing
```python
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
```

#### Power Calculation
```python
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
```

---

### **DAY 16: Arrays & Strings Recursion**

#### List Processing (Index-based)
```python
def process_list(lst, index=0):
    # Base case
    if index == len(lst):
        return base_value
    
    # Process current
    current = lst[index]
    
    # Combine with recursive result
    return combine(current, process_list(lst, index + 1))
```

#### List Processing (Slicing)
```python
def process_list(lst):
    # Base case
    if not lst:
        return base_value
    
    # Combine first with rest
    return combine(lst[0], process_list(lst[1:]))
```

#### Common List Patterns
```python
# Sum
def sum_list(lst, index=0):
    if index == len(lst):
        return 0
    return lst[index] + sum_list(lst, index + 1)

# Min
def min_list(lst, index=0):
    if index == len(lst) - 1:
        return lst[index]
    return min(lst[index], min_list(lst, index + 1))

# Check sorted
def is_sorted(lst, index=0):
    if index == len(lst) - 1:
        return True
    if lst[index] > lst[index + 1]:
        return False
    return is_sorted(lst, index + 1)
```

#### String Recursion
```python
# Reverse
def reverse_string(text):
    if not text:
        return ""
    return reverse_string(text[1:]) + text[0]

# Count vowels
def count_vowels(text, index=0):
    if index == len(text):
        return 0
    count = 1 if text[index] in "aeiouAEIOU" else 0
    return count + count_vowels(text, index + 1)

# Palindrome
def is_palindrome(text, left=0, right=None):
    if right is None:
        right = len(text) - 1
    if left >= right:
        return True
    if text[left] != text[right]:
        return False
    return is_palindrome(text, left + 1, right - 1)
```

---

### **DAY 17: Advanced Recursion**

#### Fibonacci (Multiple Recursive Calls)
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

#### GCD (Euclidean Algorithm)
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

#### Prime Check (Recursive)
```python
def is_prime_helper(n, divisor=2):
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime_helper(n, divisor + 1)

def is_prime(num):
    if num < 2:
        return False
    return is_prime_helper(num)
```

#### Search Patterns
```python
# First occurrence
def first_occurrence(lst, target, index=0):
    if index == len(lst):
        return -1
    if lst[index] == target:
        return index
    return first_occurrence(lst, target, index + 1)

# Last occurrence
def last_occurrence(lst, target, index=0):
    if index == len(lst):
        return -1
    rest = last_occurrence(lst, target, index + 1)
    if rest != -1:
        return rest
    if lst[index] == target:
        return index
    return -1

# Count occurrences
def count_occurrences(lst, target, index=0):
    if index == len(lst):
        return 0
    count = 1 if lst[index] == target else 0
    return count + count_occurrences(lst, target, index + 1)
```

---

<a name="patterns"></a>
## 🎯 QUICK REFERENCE PATTERNS

### Loop Patterns
```python
# Accumulator (Sum/Product)
total = 0
for item in items:
    total += item

# Counter
count = 0
for item in items:
    if condition:
        count += 1

# Finding Max/Min
max_val = items[0]
for item in items:
    if item > max_val:
        max_val = item

# Building Result
result = ""
for char in text:
    if condition:
        result += char
```

### Dictionary Patterns
```python
# Frequency Counter
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Grouping
groups = {}
for item in items:
    key = get_key(item)
    groups.setdefault(key, [])
    groups[key].append(item)

# Inversion
inverted = {}
for key, value in original.items():
    inverted[value] = key
```

### Recursion Patterns
```python
# Print-based
def print_pattern(n):
    if n == 0:
        return
    # Print before or after recursive call
    print_pattern(n - 1)

# Return-based
def calculate(n):
    if n == base:
        return base_value
    return current + calculate(n - 1)

# List processing
def process(lst, index=0):
    if index == len(lst):
        return base
    return combine(lst[index], process(lst, index+1))
```

---

<a name="mistakes"></a>
## ⚠️ COMMON MISTAKES TO AVOID

### 1. Input Type Mistakes
```python
# WRONG
age = input("Enter age: ")
if age > 18:  # ERROR: comparing string to int

# RIGHT
age = int(input("Enter age: "))
if age > 18:  # Works!
```

### 2. Modifying List While Iterating
```python
# WRONG
for item in lst:
    lst.remove(item)  # Dangerous!

# RIGHT
for item in lst[:]:  # Copy
    lst.remove(item)
# OR
lst = [item for item in lst if condition]
```

### 3. Forgetting Return
```python
# WRONG
def add(a, b):
    a + b  # Nothing returned!

# RIGHT
def add(a, b):
    return a + b
```

### 4. Recursion Without Base Case
```python
# WRONG
def count_down(n):
    print(n)
    count_down(n - 1)  # Infinite!

# RIGHT
def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n - 1)
```

### 5. Using = Instead of ==
```python
# WRONG
if x = 5:  # Assignment, not comparison!

# RIGHT
if x == 5:  # Comparison
```

---

## 📊 SUMMARY

### You've Mastered:
✅ Variables, data types, input/output  
✅ Conditionals (if/elif/else)  
✅ Strings and string methods  
✅ Lists, tuples, sets  
✅ Loops (for/while)  
✅ Dictionaries and hash maps  
✅ Comprehensions  
✅ Functions (parameters, return)  
✅ Recursion (all levels)  
✅ Basic algorithms  

### Total Progress:
- **129 programs written**
- **17 days completed**
- **4 major modules mastered**

### Next Up:
- **OOP (Classes & Objects)**
- **File Handling**
- **Then AI Projects!**

---

**Last Updated:** December 31, 2025  
**Created by:** Aayush (with Claude's guidance)  
**Purpose:** Complete reference for Python fundamentals

**Keep this handy for quick lookups!** 📖
