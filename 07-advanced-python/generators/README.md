# Generators - Lazy Evaluation & Memory Efficiency

Master generators for streaming AI responses and processing large datasets.

## 🎯 Why Generators for AI?

✅ **Streaming LLM responses** - Yield tokens as generated  
✅ **Large dataset processing** - Handle data that doesn't fit in memory  
✅ **RAG pipelines** - Process documents chunk by chunk  
✅ **Memory efficiency** - Critical for production systems  

## 📚 Learning Levels

| Level | Days | Programs | Focus |
|-------|------|----------|-------|
| 1 | 40 | 3 | `yield` basics |
| 2 | 41 | 4 | Iteration & `next()` |
| 3 | 42 | 3 | Execution flow |
| 4 | 43 | 3 | Logic & conditions |
| 5 | 44 | 3 | Advanced logic |
| 6 | 46 | 5 | Advanced patterns |

## 🔑 Key Concepts

### Generator vs List

| Feature | List | Generator |
|---------|------|-----------|
| **Memory** | Stores all | Stores current only |
| **Execution** | Immediate | Lazy (on-demand) |
| **Use Case** | Small data | Large/infinite data |

### Basic Syntax
```python
# List (eager)
def squares_list(n):
    return [i*i for i in range(n)]

# Generator (lazy)
def squares_gen(n):
    for i in range(n):
        yield i*i
```

## 📁 Structure
```
day-40-generator-basics-1/    # 3 programs
day-41-generator-basics-2/    # 4 programs
day-42-execution-flow/        # 3 programs
day-43-logic-conditions-1/    # 3 programs
day-44-logic-conditions-2/    # 3 programs
day-46-advanced-patterns/     # 5 programs
```

## 📊 Progress

- [x] Day 40: Basics Part 1 (3) ✅
- [x] Day 41: Basics Part 2 (4) ✅
- [x] Day 42: Execution Flow (3) ✅
- [x] Day 43: Logic Part 1 (3) ✅
- [x] Day 44: Logic Part 2 (3) ✅
- [x] Day 46: Advanced Patterns (5) ✅

**Total:** 21 programs ✅ **COMPLETE**

## 🎯 Advanced Patterns Covered

### Generator Pipelines
```python
# Chain generators for data processing
source = number_source(100)
filtered = filter_evens(source)
transformed = square_numbers(filtered)
```

### Two-Way Communication
```python
# Use .send() for interactive generators
gen = interactive_gen()
gen.send("message")
```

### Delegation
```python
# Use yield from for cleaner code
def main_gen():
    yield from sub_gen()
```

---

**Days:** 40-46/222 | **Status:** ✅ COMPLETE 
