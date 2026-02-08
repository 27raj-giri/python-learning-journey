# Python File I/O - Complete Reference

**Days:** 18-23 | **Programs:** 30 | **Status:** ✅ COMPLETE

---

## Table of Contents

1. [File Modes](#file-modes)
2. [Basic Operations](#basic-operations)
3. [Reading Patterns](#reading-patterns)
4. [Writing Patterns](#writing-patterns)
5. [Processing Patterns](#processing-patterns)
6. [Best Practices](#best-practices)
7. [Common Patterns](#common-patterns)
8. [Interview Questions](#interview-questions)

---

## File Modes

| Mode | Meaning | Creates File? | Overwrites? | Read | Write |
|------|---------|---------------|-------------|------|-------|
| `'r'` | Read | ❌ (Error if missing) | N/A | ✅ | ❌ |
| `'w'` | Write | ✅ | ✅ YES | ❌ | ✅ |
| `'a'` | Append | ✅ | ❌ (adds to end) | ❌ | ✅ |
| `'r+'` | Read+Write | ❌ | ❌ | ✅ | ✅ |
| `'w+'` | Write+Read | ✅ | ✅ YES | ✅ | ✅ |
| `'a+'` | Append+Read | ✅ | ❌ | ✅ | ✅ |

**Remember:** `w` = DANGER (overwrites everything!)

---

## Basic Operations

### Opening Files
```python
# Basic (manual close needed)
file = open('data.txt', 'r')
content = file.read()
file.close()

# With statement (auto-closes) ⭐ BEST PRACTICE
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed
```

### Reading Methods
```python
# Read entire file as string
content = file.read()

# Read one line
line = file.readline()

# Read all lines as list
lines = file.readlines()  # ['line1\n', 'line2\n', ...]
```

### Writing Methods
```python
# Write string
file.write('Hello\n')

# Write multiple lines
file.writelines(['Line 1\n', 'Line 2\n'])
```

---

## Reading Patterns

### Pattern 1: Read Entire File
```python
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
```

**Use when:** Small files, need everything at once

---

### Pattern 2: Line-by-Line (Memory Efficient)
```python
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Remove \n
```

**Use when:** Large files, process line by line

---

### Pattern 3: Read as List
```python
with open('file.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

**Use when:** Need to modify/reorder lines

---

### Pattern 4: Count Lines
```python
with open('file.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
    print(f"Total lines: {count}")
```

---

### Pattern 5: Filter Lines
```python
# Find lines containing keyword
with open('file.txt', 'r') as f:
    for line in f:
        if 'ERROR' in line:
            print(line.strip())
```

---

## Writing Patterns

### Pattern 1: Create New File
```python
with open('output.txt', 'w') as f:
    f.write('Hello World\n')
    f.write('Line 2\n')
```

**Warning:** Overwrites existing file!

---

### Pattern 2: Append to File
```python
with open('log.txt', 'a') as f:
    f.write('New log entry\n')
```

---

### Pattern 3: Write Numbers
```python
with open('numbers.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f'{i}\n')
```

---

### Pattern 4: Write List
```python
names = ['Alice', 'Bob', 'Charlie']
with open('names.txt', 'w') as f:
    for name in names:
        f.write(f'{name}\n')
```

---

## Processing Patterns

### Pattern 1: Process Numbers
```python
# Read numbers and calculate sum
total = 0
with open('numbers.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        total += num
print(f'Sum: {total}')
```

---

### Pattern 2: Transform Text
```python
# Convert to uppercase
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        for line in inp:
            out.write(line.upper())
```

---

### Pattern 3: Filter and Copy
```python
# Copy only long lines
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        for line in inp:
            if len(line.strip()) > 10:
                out.write(line)
```

---

### Pattern 4: Count Words
```python
word_count = 0
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        word_count += len(words)
print(f'Total words: {word_count}')
```

---

### Pattern 5: Find Maximum
```python
# Find max number in file
max_num = float('-inf')
with open('numbers.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        if num > max_num:
            max_num = num
print(f'Maximum: {max_num}')
```

---

## Best Practices

### 1. Always Use `with` Statement ⭐
```python
# ❌ BAD - Manual close
file = open('data.txt', 'r')
content = file.read()
file.close()

# ✅ GOOD - Auto-close
with open('data.txt', 'r') as file:
    content = file.read()
```

---

### 2. Strip Whitespace
```python
# ❌ BAD - Extra \n
for line in file:
    print(line)  # "Hello\n"

# ✅ GOOD - Clean
for line in file:
    print(line.strip())  # "Hello"
```

---

### 3. Error Handling
```python
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found!')
```

---

### 4. Type Conversion
```python
# Numbers come as strings!
with open('numbers.txt', 'r') as f:
    for line in f:
        num = int(line.strip())  # Convert!
        print(num * 2)
```

---

## Common Patterns Quick Reference

### Copy File
```python
with open('source.txt', 'r') as src:
    with open('dest.txt', 'w') as dst:
        dst.write(src.read())
```

### Merge Two Files
```python
with open('file1.txt', 'r') as f1:
    with open('file2.txt', 'r') as f2:
        with open('merged.txt', 'w') as out:
            out.write(f1.read())
            out.write(f2.read())
```

### Replace Text
```python
with open('input.txt', 'r') as inp:
    content = inp.read()
    content = content.replace('old', 'new')
    
with open('output.txt', 'w') as out:
    out.write(content)
```

### Remove Duplicates
```python
seen = set()
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        for line in inp:
            if line not in seen:
                out.write(line)
                seen.add(line)
```

### Count Specific Words
```python
count = 0
with open('file.txt', 'r') as f:
    for line in f:
        count += line.lower().count('error')
print(f'ERROR count: {count}')
```

---

## Interview Questions

### Q1: Difference between `read()`, `readline()`, `readlines()`?

- **`read()`** - Returns entire file as one string
- **`readline()`** - Returns one line as string
- **`readlines()`** - Returns list of all lines

---

### Q2: Why use `with` statement?

- Auto-closes file (even if error occurs)
- Prevents resource leaks
- Cleaner code

---

### Q3: What happens if file doesn't exist?

- **Read mode (`'r'`)** - FileNotFoundError
- **Write/Append (`'w'`, `'a'`)** - Creates new file

---

### Q4: How to check if file exists?
```python
import os
if os.path.exists('file.txt'):
    # File exists
```

---

### Q5: How to get file size?
```python
import os
size = os.path.getsize('file.txt')
print(f'Size: {size} bytes')
```

---

## Summary

**30 Programs Covering:**
- ✅ File modes (r, w, a)
- ✅ Reading (read, readline, readlines)
- ✅ Writing (write, writelines)
- ✅ Line-by-line processing
- ✅ Number processing
- ✅ Text transformation
- ✅ Multiple file operations
- ✅ Error handling
- ✅ Best practices (with statement)

**Key Takeaway:** Always use `with` statement for file operations!

---

**Days:** 18-23 | **Next:** OOP (Days 24-39) 
