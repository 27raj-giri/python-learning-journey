# Day 22 - File I/O Level 5: Real-World Applications

**Date:** January 5, 2026  
**Programs:** 5  
**Time:** 1-1.5 hours  
**Focus:** Practical file operations, multiple files

---

## 🎯 Topics Covered

- Copying files
- Merging multiple files
- Log file analysis
- Student records processing
- Building mini applications

---

## 📝 Programs

### 21. copy_file.py
**Concept:** Copy content from one file to another  
**Key Methods:** `read()`, `write()`  
**Purpose:** File backup/duplication

### 22. merge_files.py
**Concept:** Merge two text files into one  
**Key Methods:** multiple `read()`, single `write()`  
**Purpose:** Combining data sources

### 23. count_error_logs.py
**Concept:** Count "ERROR" occurrences in log file  
**Key Methods:** string counting, conditionals  
**Purpose:** Log file analysis

### 24. student_marks_topper.py
**Concept:** Store names & marks, find topper  
**Key Methods:** file parsing, `max()` logic  
**Purpose:** Data processing

### 25. contact_book.py
**Concept:** File-based contact book (add, view)  
**Key Methods:** append, read, user input loop  
**Purpose:** Simple CRUD application

---

## 🔑 Key Learnings

### Copy file pattern:
```python
source = open('source.txt', 'r')
destination = open('destination.txt', 'w')

destination.write(source.read())

source.close()
destination.close()
```

### Merge files pattern:
```python
file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')
merged = open('merged.txt', 'w')

merged.write(file1.read())
merged.write(file2.read())
```

### Simple application structure:
```python
while True:
    choice = input("Menu: ")
    if choice == '1':
        # Add data
    elif choice == '2':
        # View data
    elif choice == 'exit':
        break
```

---

## 💡 Real-World Use Cases

**Log Analysis:**
- Count errors, warnings
- Find patterns
- Generate reports

**Data Management:**
- Student records
- Contact books
- Simple databases

**File Operations:**
- Backup files
- Merge data
- Split data

---

## 🚧 Challenges Faced

- Building interactive menu systems
- Handling file existence checks
- Parsing structured data from files

---

## ✅ Progress

- [x] Level 1: Basics (Day 18)
- [x] Level 2: Logic (Day 19)
- [x] Level 3: Numbers (Day 20)
- [x] Level 4: Strings (Day 21)
- [x] Level 5: Advanced (Day 22)
- [ ] Level 6: Powerful (Day 23)

**Total Programs So Far:** 154/159  
**Next:** Day 23 - Optional but Powerful (Final!)