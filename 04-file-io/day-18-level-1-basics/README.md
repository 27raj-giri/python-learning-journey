# Day 18 - File I/O Level 1: Absolute Basics

**Date:** January 1, 2026  
**Programs:** 5  
**Time:** 1 hour  
**Focus:** File creation, reading, writing, modes

---

## 🎯 Topics Covered

- Creating files with `open()`
- File opening modes: `r`, `w`, `a`
- `read()` method - read entire file
- `write()` method - write to file
- `readline()` - read one line
- `close()` - always close files!
- Newline character `\n`

---

## 📝 Programs

### 1. create_and_write.py
**Concept:** Create file and write personal info  
**Key Methods:** `open()`, `write()`, `close()`  
**Creates:** `intro.txt`

### 2. read_entire_file.py
**Concept:** Read complete file content  
**Key Methods:** `read()`  
**Reads:** `intro.txt`

### 3. write_numbers.py
**Concept:** Write numbers 1-5, each on new line  
**Key Methods:** `write()`, loop, `str()`  
**Creates:** `numbers.txt`

### 4. read_line_by_line.py
**Concept:** Read and print each line separately  
**Key Methods:** `readline()`, iteration  
**Reads:** `numbers.txt`

### 5. append_to_file.py
**Concept:** Add content without overwriting  
**Key Methods:** append mode `'a'`  
**Modifies:** `intro.txt`

---

## 🔑 Key Learnings

### File Modes:
- `'r'` - Read only (file must exist)
- `'w'` - Write (overwrites if exists)
- `'a'` - Append (adds to end)

### Always close files:
```python
file = open('file.txt', 'r')
# ... do something
file.close()  # Don't forget!
```

### Writing requires string:
```python
file.write(str(123))  # Convert numbers to string
```

---

## 💡 Common Patterns

**Read entire file:**
```python
file = open('file.txt', 'r')
content = file.read()
file.close()
```

**Write to file:**
```python
file = open('file.txt', 'w')
file.write('Hello World\n')
file.close()
```

**Append to file:**
```python
file = open('file.txt', 'a')
file.write('New line\n')
file.close()
```

---

## 🚧 Challenges Faced

- Understanding when to use `'w'` vs `'a'`
- Remembering to add `\n` for new lines
- Forgetting to close files
- Converting numbers to strings before writing

---

## ✅ Progress

- [x] Level 1: Basics (Day 18)
- [ ] Level 2: Logic (Day 19)
- [ ] Level 3: Numbers (Day 20)
- [ ] Level 4: Strings (Day 21)
- [ ] Level 5: Advanced (Day 22)
- [ ] Level 6: Powerful (Day 23)

**Total Programs So Far:** 134/159  
**Next:** Day 19 - Reading with Logic