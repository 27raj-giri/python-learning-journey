# Day 19 - File I/O Level 2: Reading with Logic

**Date:** January 2, 2026  
**Programs:** 5  
**Time:** 1 hour  
**Focus:** Conditional reading, counting, filtering

---

## 🎯 Topics Covered

- Counting lines in files
- Counting words using `split()`
- Counting characters with `len()`
- Filtering lines by keyword
- Filtering lines by length
- Conditional file processing

---

## 📝 Programs

### 6. count_lines.py
**Concept:** Count total lines in file  
**Key Methods:** iteration, counter pattern  
**Uses:** `intro.txt`

### 7. count_words.py
**Concept:** Count total words in file  
**Key Methods:** `split()`, `len()`  
**Uses:** `intro.txt`

### 8. count_characters.py
**Concept:** Count characters (with/without spaces)  
**Key Methods:** `len()`, `replace()`  
**Uses:** `intro.txt`

### 9. filter_by_keyword.py
**Concept:** Print only lines containing "Python"  
**Key Methods:** `in` operator, conditionals  
**Creates/Uses:** `languages.txt`

### 10. filter_by_length.py
**Concept:** Print lines longer than 20 chars  
**Key Methods:** `len()`, conditionals  
**Uses:** `languages.txt`

---

## 🔑 Key Learnings

### Counting patterns:
```python
# Count lines
count = 0
for line in file:
    count += 1

# Count words
words = content.split()
word_count = len(words)

# Count characters
char_count = len(content)
```

### Filtering pattern:
```python
for line in file:
    if 'keyword' in line:
        print(line.strip())
```

### strip() is your friend:
- Removes `\n` and extra spaces
- Use before printing or processing

---

## 💡 Common Patterns

**Count lines:**
```python
file = open('file.txt', 'r')
count = sum(1 for line in file)
file.close()
```

**Filter by condition:**
```python
for line in file:
    if condition:
        print(line.strip())
```

---

## 🚧 Challenges Faced

- Deciding whether to count spaces/newlines
- Understanding `split()` vs `splitlines()`
- Using `strip()` correctly

---

## ✅ Progress

- [x] Level 1: Basics (Day 18)
- [x] Level 2: Logic (Day 19)
- [ ] Level 3: Numbers (Day 20)
- [ ] Level 4: Strings (Day 21)
- [ ] Level 5: Advanced (Day 22)
- [ ] Level 6: Powerful (Day 23)

**Total Programs So Far:** 139/159  
**Next:** Day 20 - Numbers + Files