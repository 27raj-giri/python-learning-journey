# Day 44: Generators with Logic Part 2

Advanced logic patterns and memory-efficient generation.

## 🎯 Concepts

- Complex filtering logic
- Unique element generation
- Prime number algorithm
- Memory efficiency demo

## 📚 Programs (3)

| # | Program | Concept |
|---|---------|---------|
| 14 | Unique Elements | Remove duplicates lazily |
| 15 | Prime Generator | Advanced logic |
| 16 | Million Numbers | Memory efficiency |

## 💡 Key Learning

### Unique Elements
```python
def unique_gen(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item
```

### Memory Efficiency
```python
# List - uses ~8MB for 1M numbers
nums_list = list(range(1000000))

# Generator - uses ~128 bytes
nums_gen = (i for i in range(1000000))
```

## 🚀 Run
```bash
python 14_unique_elements.py
python 15_prime_generator.py
python 16_million_numbers.py
```

## 📊 Features

✅ Advanced filtering  
✅ Algorithm implementation  
✅ Memory optimization  
✅ Production patterns  

---

**Day:** 44 | **Programs:** 3/3  
**Next:** Day 45 (Memory & Advanced)
