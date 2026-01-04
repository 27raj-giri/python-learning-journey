# Day 21 - File I/O Level 4: Files + Strings

**Date:** January 4, 2026  
**Programs:** 5  
**Time:** 1-1.5 hours  
**Focus:** String processing with files (Interview Favorite!)

---

## 🎯 Topics Covered

- Text transformation (uppercase, replace)
- Finding most frequent words
- Removing duplicate lines
- String reversal in files
- Dictionary-based word counting

---

## 📝 Programs

### 16. uppercase_file.py
**Concept:** Convert to uppercase, save to new file  
**Key Methods:** `upper()`, reading/writing  
**Creates:** `uppercase_output.txt`

### 17. replace_spaces.py
**Concept:** Replace spaces with underscores  
**Key Methods:** `replace()`, file transformation  
**Creates:** `underscore_output.txt`

### 18. most_frequent_word.py
**Concept:** Find most common word  
**Key Methods:** dictionary counting, `max()`  
**Uses:** `words_file.txt`

### 19. remove_duplicates.py
**Concept:** Remove duplicate lines from file  
**Key Methods:** `set()`, preserving order  
**Creates:** `unique_output.txt`

### 20. reverse_lines.py
**Concept:** Reverse each line, write to new file  
**Key Methods:** string slicing `[::-1]`  
**Creates:** `reversed_lines.txt`

---

## 🔑 Key Learnings

### String transformation pattern:
```python
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

for line in input_file:
    transformed = line.upper()
    output_file.write(transformed)

input_file.close()
output_file.close()
```

### Frequency counting:
```python
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_frequent = max(word_count, key=word_count.get)
```

### Remove duplicates (preserve order):
```python
seen = set()
unique = []
for line in file:
    if line not in seen:
        seen.add(line)
        unique.append(line)
```

---

## 💡 Common Patterns

**Transform and save:**
```python
for line in input_file:
    output_file.write(line.upper())
```

**Count frequency:**
```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```

---

## 🚧 Challenges Faced

- Managing input/output file names
- Dictionary operations for counting
- Deciding whether to preserve original file

---

## ✅ Progress

- [x] Level 1: Basics (Day 18)
- [x] Level 2: Logic (Day 19)
- [x] Level 3: Numbers (Day 20)
- [x] Level 4: Strings (Day 21)
- [ ] Level 5: Advanced (Day 22)
- [ ] Level 6: Powerful (Day 23)

**Total Programs So Far:** 149/159  
**Next:** Day 22 - Real-World Applications