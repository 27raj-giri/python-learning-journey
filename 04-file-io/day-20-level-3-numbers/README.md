# Day 20 - File I/O Level 3: Numbers + Files

**Date:** January 3, 2026  
**Programs:** 5  
**Time:** 1 hour  
**Focus:** Numerical data processing from files

---

## 🎯 Topics Covered

- Writing large number sequences
- Reading numbers from files
- Mathematical operations (sum, max)
- Type conversion: `int(line.strip())`
- Filtering even/odd numbers
- Writing to multiple files simultaneously

---

## 📝 Programs

### 11. write_1_to_100.py
**Concept:** Generate file with numbers 1-100  
**Key Methods:** `range()`, `write()`, `str()`  
**Creates:** `hundred.txt`

### 12. sum_from_file.py
**Concept:** Calculate sum of all numbers  
**Key Methods:** `int()`, accumulator pattern  
**Uses:** `hundred.txt`

### 13. max_from_file.py
**Concept:** Find maximum number  
**Key Methods:** comparison, `max()` function  
**Uses:** `hundred.txt`

### 14. count_even_numbers.py
**Concept:** Count even numbers in file  
**Key Methods:** modulo `%`, conditionals  
**Uses:** `hundred.txt`

### 15. separate_even_odd.py
**Concept:** Split numbers into two files  
**Key Methods:** multiple file handles  
**Creates:** `even_numbers.txt`, `odd_numbers.txt`

---

## 🔑 Key Learnings

### Number processing pattern:
```python
file = open('numbers.txt', 'r')
total = 0
for line in file:
    num = int(line.strip())  # Must convert!
    total += num
file.close()
```

### Multiple files pattern:
```python
file1 = open('even.txt', 'w')
file2 = open('odd.txt', 'w')

# ... process

file1.close()
file2.close()  # Close all!
```

### Always strip() before int():
```python
num = int(line.strip())  # Removes \n
```

---

## 💡 Common Patterns

**Read and sum:**
```python
total = 0
for line in file:
    total += int(line.strip())
```

**Find maximum manually:**
```python
maximum = float('-inf')
for line in file:
    num = int(line.strip())
    if num > maximum:
        maximum = num
```

---

## 🚧 Challenges Faced

- Forgetting to convert string to int
- Managing multiple file objects
- Remembering to close ALL opened files

---

## ✅ Progress

- [x] Level 1: Basics (Day 18)
- [x] Level 2: Logic (Day 19)
- [x] Level 3: Numbers (Day 20)
- [ ] Level 4: Strings (Day 21)
- [ ] Level 5: Advanced (Day 22)
- [ ] Level 6: Powerful (Day 23)

**Total Programs So Far:** 144/159  
**Next:** Day 21 - Files + Strings (Interview Favorite!)