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
| 6 | 45 | 3-4 | Memory patterns (optional) |

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
day-45-memory-advanced/       # 3-4 programs (optional)
```

## 📊 Progress

- [ ] Day 40: Basics Part 1 (3)
- [ ] Day 41: Basics Part 2 (4)
- [ ] Day 42: Execution Flow (3)
- [ ] Day 43: Logic Part 1 (3)
- [ ] Day 44: Logic Part 2 (3)
- [ ] Day 45: Advanced (3-4) - Optional

**Total:** 16-20 programs

---

**Days:** 40-45 | **Next:** Decorators (Day 46)
```
