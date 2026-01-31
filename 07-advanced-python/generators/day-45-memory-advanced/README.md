# Day 45: Memory & Advanced Patterns

Real-world memory efficiency and advanced generator patterns.

## 🎯 Concepts

- File processing without full load
- Lazy evaluation in practice
- Memory comparison (list vs generator)
- Infinite sequences

## 📚 Programs (3-4)

| # | Program | Concept |
|---|---------|---------|
| 17 | File Line Reader | Process files lazily |
| 18 | Lazy Squares | On-demand computation |
| 19 | Memory Comparison | List vs Generator demo |
| 20 | Infinite Evens | Infinite sequences (optional) |

## 💡 Key Learning

### File Processing
```python
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()  # Process one line at a time
```

### Why Generators Matter
```python
# List - loads everything in memory
data = [process(line) for line in huge_file]  # ❌ Memory overflow

# Generator - processes on demand
data = (process(line) for line in huge_file)  # ✅ Memory efficient
```

## 🚀 Run
```bash
python 17_file_line_reader.py
python 18_lazy_squares.py
python 19_memory_comparison.py
python 20_infinite_evens.py  # Optional
```

## 📊 Features

✅ Real-world file processing  
✅ Memory optimization  
✅ Lazy evaluation patterns  
✅ Production-ready code  

---

**Day:** 45 | **Programs:** 3-4
